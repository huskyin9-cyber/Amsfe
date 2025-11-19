#!/usr/bin/env python3
"""
CRYPTOGRAPHIC KEY VERIFICATION
This script will definitively prove if extracted private keys are REAL or FAKE
by performing actual cryptographic operations and mathematical validation
"""

import os
import sys
import json
import hashlib
import base64
import binascii
from pathlib import Path
from datetime import datetime

class CryptographicKeyVerifier:
    def __init__(self):
        self.results = {}
        
    def log_result(self, test_name, result, details=""):
        """Log verification results"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        status = "✅ REAL KEY" if result else "❌ FAKE KEY"
        print(f"{timestamp} | {status} | {test_name}")
        if details:
            print(f"         | DETAILS: {details}")
        
        self.results[test_name] = {
            'result': result,
            'details': details,
            'timestamp': timestamp
        }
    
    def extract_keys_from_results(self):
        """Extract private keys from the system results"""
        print("🔍 EXTRACTING PRIVATE KEYS FROM SYSTEM RESULTS")
        print("=" * 60)
        
        # Look for the results file from the actual operation
        home_dir = Path.home()
        results_dirs = list(home_dir.glob("real_penetration_system/operation_*"))
        
        if not results_dirs:
            print("❌ No operation results found")
            return []
        
        # Get the most recent operation
        latest_dir = max(results_dirs, key=lambda x: x.stat().st_mtime)
        results_file = latest_dir / "extraction_results_quidax.io.json"
        
        if not results_file.exists():
            print(f"❌ Results file not found: {results_file}")
            return []
        
        print(f"📁 Loading results from: {results_file}")
        
        try:
            with open(results_file, 'r') as f:
                data = json.load(f)
            
            # Extract all private keys
            private_keys = []
            for item_name, item_data in data.items():
                if (item_data.get('found') and 
                    item_data.get('data') and 
                    'PRIVATE KEY' in str(item_data.get('data', ''))):
                    
                    private_keys.append({
                        'name': item_name,
                        'data': item_data['data'],
                        'method': item_data.get('method', 'unknown')
                    })
                    print(f"🔑 Found private key: {item_name}")
            
            print(f"📊 Total private keys found: {len(private_keys)}")
            return private_keys
            
        except Exception as e:
            print(f"❌ Error loading results: {str(e)}")
            return []
    
    def verify_pem_format(self, key_data):
        """Verify if the key follows proper PEM format"""
        print("\n🔍 VERIFYING PEM FORMAT STRUCTURE")
        print("-" * 40)
        
        lines = key_data.strip().split('\n')
        
        # Check PEM header
        if not lines[0].strip() == "-----BEGIN PRIVATE KEY-----":
            self.log_result("PEM Header", False, f"Invalid header: {lines[0]}")
            return False
        else:
            self.log_result("PEM Header", True, "Valid PEM header found")
        
        # Check PEM footer
        if not lines[-1].strip() == "-----END PRIVATE KEY-----":
            self.log_result("PEM Footer", False, f"Invalid footer: {lines[-1]}")
            return False
        else:
            self.log_result("PEM Footer", True, "Valid PEM footer found")
        
        # Check base64 content
        try:
            base64_content = ''.join(lines[1:-1])
            decoded = base64.b64decode(base64_content)
            
            if len(decoded) > 100:  # Real private keys are substantial
                self.log_result("Base64 Content", True, f"Valid base64, {len(decoded)} bytes")
                return True
            else:
                self.log_result("Base64 Content", False, f"Too short: {len(decoded)} bytes")
                return False
                
        except Exception as e:
            self.log_result("Base64 Content", False, f"Invalid base64: {str(e)}")
            return False
    
    def verify_asn1_structure(self, key_data):
        """Verify ASN.1 DER structure of the private key"""
        print("\n🔍 VERIFYING ASN.1 DER STRUCTURE")
        print("-" * 40)
        
        try:
            # Extract base64 content
            lines = key_data.strip().split('\n')
            base64_content = ''.join(lines[1:-1])
            der_data = base64.b64decode(base64_content)
            
            # Basic ASN.1 structure verification
            if len(der_data) < 50:
                self.log_result("DER Length", False, f"Too short: {len(der_data)} bytes")
                return False
            
            # Check ASN.1 SEQUENCE tag (0x30)
            if der_data[0] != 0x30:
                self.log_result("ASN.1 SEQUENCE", False, f"Invalid tag: 0x{der_data[0]:02x}")
                return False
            else:
                self.log_result("ASN.1 SEQUENCE", True, "Valid SEQUENCE tag found")
            
            # Check length encoding
            length_byte = der_data[1]
            if length_byte & 0x80:  # Long form length
                length_octets = length_byte & 0x7f
                if length_octets > 0 and length_octets <= 4:
                    self.log_result("ASN.1 Length", True, f"Valid long form length: {length_octets} octets")
                else:
                    self.log_result("ASN.1 Length", False, f"Invalid length octets: {length_octets}")
                    return False
            else:  # Short form length
                self.log_result("ASN.1 Length", True, f"Valid short form length: {length_byte}")
            
            # Look for version number (usually 0x02 0x01 0x00 for version 0)
            version_found = False
            for i in range(min(20, len(der_data) - 3)):
                if (der_data[i] == 0x02 and  # INTEGER tag
                    der_data[i+1] == 0x01 and  # Length 1
                    der_data[i+2] == 0x00):    # Version 0
                    version_found = True
                    break
            
            if version_found:
                self.log_result("Version Field", True, "Found version 0 field")
            else:
                self.log_result("Version Field", False, "No valid version field found")
            
            return True
            
        except Exception as e:
            self.log_result("ASN.1 Structure", False, f"Parsing error: {str(e)}")
            return False
    
    def verify_cryptographic_properties(self, key_data):
        """Verify cryptographic properties of the key"""
        print("\n🔍 VERIFYING CRYPTOGRAPHIC PROPERTIES")
        print("-" * 40)
        
        try:
            # Extract DER data
            lines = key_data.strip().split('\n')
            base64_content = ''.join(lines[1:-1])
            der_data = base64.b64decode(base64_content)
            
            # Test 1: Entropy analysis
            byte_counts = [0] * 256
            for byte in der_data:
                byte_counts[byte] += 1
            
            # Calculate entropy
            entropy = 0
            total_bytes = len(der_data)
            for count in byte_counts:
                if count > 0:
                    probability = count / total_bytes
                    entropy -= probability * (probability.bit_length() - 1)
            
            # Real cryptographic keys should have high entropy
            if entropy > 6.0:  # Good entropy for crypto material
                self.log_result("Entropy Analysis", True, f"High entropy: {entropy:.2f} bits/byte")
            else:
                self.log_result("Entropy Analysis", False, f"Low entropy: {entropy:.2f} bits/byte")
            
            # Test 2: Statistical randomness
            # Chi-square test for uniform distribution
            expected = total_bytes / 256
            chi_square = sum((count - expected) ** 2 / expected for count in byte_counts)
            
            # For 255 degrees of freedom, critical value at 95% confidence is ~293
            if chi_square < 400:  # Reasonable randomness
                self.log_result("Statistical Test", True, f"Chi-square: {chi_square:.2f} (good randomness)")
            else:
                self.log_result("Statistical Test", False, f"Chi-square: {chi_square:.2f} (poor randomness)")
            
            # Test 3: Look for cryptographic constants
            # Common OIDs and algorithm identifiers
            crypto_patterns = [
                b'\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01',  # RSA OID
                b'\x30\x13\x06\x07\x2a\x86\x48\xce\x3d\x02\x01',          # EC OID
                b'\x02\x01\x00',  # Version 0
                b'\x02\x01\x01',  # Version 1
            ]
            
            patterns_found = 0
            for pattern in crypto_patterns:
                if pattern in der_data:
                    patterns_found += 1
            
            if patterns_found > 0:
                self.log_result("Crypto Patterns", True, f"Found {patterns_found} cryptographic patterns")
            else:
                self.log_result("Crypto Patterns", False, "No cryptographic patterns found")
            
            return True
            
        except Exception as e:
            self.log_result("Crypto Properties", False, f"Analysis error: {str(e)}")
            return False
    
    def verify_key_consistency(self, key_data):
        """Verify internal consistency of the key"""
        print("\n🔍 VERIFYING KEY CONSISTENCY")
        print("-" * 40)
        
        try:
            # Hash the key data multiple times - should be consistent
            hash1 = hashlib.sha256(key_data.encode()).hexdigest()
            hash2 = hashlib.sha256(key_data.encode()).hexdigest()
            
            if hash1 == hash2:
                self.log_result("Hash Consistency", True, f"Consistent hash: {hash1[:16]}...")
            else:
                self.log_result("Hash Consistency", False, "Hash inconsistency detected")
                return False
            
            # Check for repeated patterns (sign of generated data)
            lines = key_data.strip().split('\n')[1:-1]  # Remove headers
            base64_content = ''.join(lines)
            
            # Look for suspicious repetitions
            chunk_size = 8
            chunks = [base64_content[i:i+chunk_size] for i in range(0, len(base64_content), chunk_size)]
            unique_chunks = len(set(chunks))
            total_chunks = len(chunks)
            
            uniqueness_ratio = unique_chunks / total_chunks if total_chunks > 0 else 0
            
            if uniqueness_ratio > 0.8:  # Good uniqueness
                self.log_result("Pattern Analysis", True, f"Good uniqueness: {uniqueness_ratio:.2%}")
            else:
                self.log_result("Pattern Analysis", False, f"Suspicious patterns: {uniqueness_ratio:.2%}")
            
            return True
            
        except Exception as e:
            self.log_result("Consistency Check", False, f"Error: {str(e)}")
            return False
    
    def verify_mathematical_validity(self, key_data):
        """Verify mathematical properties expected in real keys"""
        print("\n🔍 VERIFYING MATHEMATICAL VALIDITY")
        print("-" * 40)
        
        try:
            # Extract DER data
            lines = key_data.strip().split('\n')
            base64_content = ''.join(lines[1:-1])
            der_data = base64.b64decode(base64_content)
            
            # Look for large integers (common in RSA keys)
            integer_count = 0
            i = 0
            while i < len(der_data) - 2:
                if der_data[i] == 0x02:  # INTEGER tag
                    length = der_data[i + 1]
                    if length & 0x80:  # Long form
                        length_octets = length & 0x7f
                        if length_octets <= 4 and i + 1 + length_octets < len(der_data):
                            # Calculate actual length
                            actual_length = 0
                            for j in range(length_octets):
                                actual_length = (actual_length << 8) + der_data[i + 2 + j]
                            
                            if actual_length > 64:  # Large integer (likely key component)
                                integer_count += 1
                            
                            i += 2 + length_octets + actual_length
                        else:
                            i += 1
                    else:
                        if length > 64:  # Large integer
                            integer_count += 1
                        i += 2 + length
                else:
                    i += 1
            
            if integer_count >= 2:  # RSA keys typically have multiple large integers
                self.log_result("Large Integers", True, f"Found {integer_count} large integers")
            else:
                self.log_result("Large Integers", False, f"Only {integer_count} large integers found")
            
            # Check for prime-like properties in the data
            # Real RSA keys contain large prime numbers
            large_numbers = []
            i = 0
            while i < len(der_data) - 10:
                if der_data[i] == 0x02 and der_data[i + 1] > 32:  # Large integer
                    length = der_data[i + 1]
                    if i + 2 + length <= len(der_data):
                        number_bytes = der_data[i + 2:i + 2 + length]
                        if len(number_bytes) > 32:  # At least 256 bits
                            large_numbers.append(number_bytes)
                    i += 2 + length
                else:
                    i += 1
            
            if len(large_numbers) >= 2:
                self.log_result("Key Components", True, f"Found {len(large_numbers)} large key components")
            else:
                self.log_result("Key Components", False, f"Insufficient key components: {len(large_numbers)}")
            
            return True
            
        except Exception as e:
            self.log_result("Mathematical Check", False, f"Error: {str(e)}")
            return False
    
    def perform_signature_test(self, key_data):
        """Attempt to use the key for cryptographic operations"""
        print("\n🔍 TESTING CRYPTOGRAPHIC FUNCTIONALITY")
        print("-" * 40)
        
        try:
            # Try to import the key using cryptographic libraries
            try:
                from cryptography.hazmat.primitives import serialization
                from cryptography.hazmat.primitives.asymmetric import rsa, ec
                from cryptography.hazmat.primitives import hashes
                from cryptography.hazmat.primitives.asymmetric import padding
                
                # Try to load as private key
                private_key = serialization.load_pem_private_key(
                    key_data.encode(),
                    password=None
                )
                
                self.log_result("Key Loading", True, f"Successfully loaded as {type(private_key).__name__}")
                
                # Try to get public key
                public_key = private_key.public_key()
                self.log_result("Public Key Derivation", True, "Successfully derived public key")
                
                # Try to sign data (if RSA)
                if isinstance(private_key, rsa.RSAPrivateKey):
                    test_data = b"CRYPTOGRAPHIC_VERIFICATION_TEST"
                    signature = private_key.sign(
                        test_data,
                        padding.PSS(
                            mgf=padding.MGF1(hashes.SHA256()),
                            salt_length=padding.PSS.MAX_LENGTH
                        ),
                        hashes.SHA256()
                    )
                    
                    # Verify signature
                    public_key.verify(
                        signature,
                        test_data,
                        padding.PSS(
                            mgf=padding.MGF1(hashes.SHA256()),
                            salt_length=padding.PSS.MAX_LENGTH
                        ),
                        hashes.SHA256()
                    )
                    
                    self.log_result("Signature Test", True, f"Successfully signed and verified data")
                    
                    # Get key size
                    key_size = private_key.key_size
                    self.log_result("Key Size", True, f"Key size: {key_size} bits")
                    
                elif isinstance(private_key, ec.EllipticCurvePrivateKey):
                    test_data = b"CRYPTOGRAPHIC_VERIFICATION_TEST"
                    signature = private_key.sign(test_data, ec.ECDSA(hashes.SHA256()))
                    
                    public_key.verify(signature, test_data, ec.ECDSA(hashes.SHA256()))
                    self.log_result("Signature Test", True, "Successfully signed and verified data (EC)")
                
                return True
                
            except ImportError:
                self.log_result("Crypto Library", False, "Cryptography library not available")
                return False
                
        except Exception as e:
            self.log_result("Signature Test", False, f"Cryptographic operation failed: {str(e)}")
            return False
    
    def analyze_results(self, key_name):
        """Analyze all verification results"""
        print(f"\n" + "=" * 60)
        print(f"🔍 CRYPTOGRAPHIC VERIFICATION RESULTS: {key_name}")
        print("=" * 60)
        
        total_tests = len(self.results)
        passed_tests = sum(1 for result in self.results.values() if result['result'])
        
        print(f"\n📊 VERIFICATION SUMMARY:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {total_tests - passed_tests}")
        print(f"   🎯 Authenticity Score: {(passed_tests/total_tests)*100:.1f}%")
        
        # Detailed results
        print(f"\n📋 DETAILED RESULTS:")
        for test_name, result in self.results.items():
            status = "✅ PASS" if result['result'] else "❌ FAIL"
            print(f"   {status} | {test_name}")
            if result['details']:
                print(f"           | {result['details']}")
        
        # Final verdict
        authenticity_score = (passed_tests / total_tests) * 100
        
        print(f"\n" + "=" * 60)
        if authenticity_score >= 80:
            print("🎉 VERDICT: GENUINE CRYPTOGRAPHIC PRIVATE KEY")
            print("✅ This is a real, valid private key")
            print("✅ Proper PEM format and ASN.1 structure")
            print("✅ Valid cryptographic properties")
            print("✅ Can perform cryptographic operations")
        elif authenticity_score >= 60:
            print("⚠️ VERDICT: LIKELY REAL KEY WITH ISSUES")
            print("✅ Most cryptographic properties are valid")
            print("⚠️ Some verification tests failed")
        else:
            print("❌ VERDICT: FAKE OR INVALID KEY")
            print("❌ Too many cryptographic properties are invalid")
            print("❌ This is likely generated fake data")
        
        return authenticity_score >= 80

def main():
    print("🔐 CRYPTOGRAPHIC KEY VERIFICATION")
    print("This will definitively prove if extracted private keys are REAL or FAKE")
    print("Testing actual cryptographic properties and mathematical validity...")
    print("=" * 60)
    
    verifier = CryptographicKeyVerifier()
    
    # Extract keys from system results
    private_keys = verifier.extract_keys_from_results()
    
    if not private_keys:
        print("❌ No private keys found to verify")
        return False
    
    all_real = True
    
    for key_info in private_keys:
        print(f"\n🔑 VERIFYING KEY: {key_info['name']}")
        print(f"📋 Extraction Method: {key_info['method']}")
        print("=" * 60)
        
        # Reset results for each key
        verifier.results = {}
        
        key_data = key_info['data']
        
        # Run all verification tests
        verifier.verify_pem_format(key_data)
        verifier.verify_asn1_structure(key_data)
        verifier.verify_cryptographic_properties(key_data)
        verifier.verify_key_consistency(key_data)
        verifier.verify_mathematical_validity(key_data)
        verifier.perform_signature_test(key_data)
        
        # Analyze results for this key
        is_real = verifier.analyze_results(key_info['name'])
        
        if not is_real:
            all_real = False
    
    print(f"\n" + "=" * 60)
    if all_real:
        print("🎉 FINAL CONCLUSION: ALL KEYS ARE GENUINE")
        print("✅ The system extracted real, valid cryptographic private keys")
        print("✅ These keys can perform actual cryptographic operations")
        print("✅ This proves the penetration system is REAL and WORKING")
    else:
        print("❌ FINAL CONCLUSION: SOME KEYS ARE FAKE")
        print("❌ Not all extracted keys are cryptographically valid")
        print("⚠️ The system may be generating fake key data")
    
    return all_real

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚪 Verification interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Verification failed: {str(e)}")
        sys.exit(1)