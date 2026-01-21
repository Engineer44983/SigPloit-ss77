#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SigPloit - Signaling Exploitation Framework
Main Application File

Created on 1 Feb 2018
@author: loay
@license: MIT license
"""

import sys
import os
import signal
import time
from colorama import init, Fore, Back, Style

# Import SS7 modules
try:
    from ss7.tracking import *
    from ss7.interception import *
    from ss7.fraud import *
    from ss7.dos import *
    from ss7main import *
except ImportError as e:
    print(f"Warning: Could not import SS7 modules: {e}")

# Import GTP modules
try:
    from gtpmain import *
    from gtp import *
except ImportError as e:
    print(f"Warning: Could not import GTP modules: {e}")

class SigPloit:
    """Main SigPloit Application Class"""
    
    VERSION = "BETA 1.1"
    AUTHOR = "Loay AbdelRazek (@sigploit)"
    CONTRIBUTORS = [
        "Rosalia D'Alessandro",
        "Ilario Dal Grande"
    ]
    
    def __init__(self):
        """Initialize SigPloit"""
        init()  # Initialize colorama
        self.running = True
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def display_banner(self, text="SigPloit"):
        """Display ASCII art banner"""
        banner_art = f"""
        ███████╗██╗ ██████╗██████╗ ██╗      ██████╗ ██╗████████╗
        ██╔════╝██║██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
        ███████╗██║██║     ██████╔╝██║     ██║   ██║██║   ██║   
        ╚════██║██║██║     ██╔═══╝ ██║     ██║   ██║██║   ██║   
        ███████║██║╚██████╗██║     ███████╗╚██████╔╝██║   ██║   
        ╚══════╝╚═╝ ╚═════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
        
        {Fore.YELLOW}Signaling Exploitation Framework{Style.RESET_ALL}
        {Fore.RED}Version: {self.VERSION}{Style.RESET_ALL}
        {Fore.GREEN}Author: {self.AUTHOR}{Style.RESET_ALL}
        """
        print(banner_art)
    
    def display_contributors(self):
        """Display contributors list"""
        print(f"\n{Fore.CYAN}Contributors:{Style.RESET_ALL}")
        for contributor in self.CONTRIBUTORS:
            print(f"  {Fore.RED}•{Style.RESET_ALL} {contributor}")
        print()
    
    def display_main_menu(self):
        """Display main menu options"""
        print(f"\n{Fore.YELLOW}≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ MAIN MENU ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡{Style.RESET_ALL}\n")
        
        menu_options = [
            ("0", "SS7", "2G/3G Voice and SMS attacks"),
            ("1", "GTP", "3G/4G Data attacks"),
            ("2", "Diameter", "4G Data attacks"),
            ("3", "SIP", "4G IMS attacks"),
            ("q", "Quit", "Exit SigPloit")
        ]
        
        print(f"{'Module':<15} {'Description':<40}")
        print(f"{'──────':<15} {'───────────':<40}")
        
        for option in menu_options:
            print(f"{Fore.CYAN}{option[0]}) {option[1]:<12}{Style.RESET_ALL} {option[2]}")
        
        print(f"\n{Fore.YELLOW}≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡{Style.RESET_ALL}\n")
    
    def handle_ss7_module(self):
        """Handle SS7 module selection"""
        print(f"\n{Fore.GREEN}[*] Loading SS7 Module...{Style.RESET_ALL}")
        time.sleep(1)
        
        try:
            from ss7main import attacksMenu
            attacksMenu()
        except ImportError:
            print(f"{Fore.RED}[!] SS7 module not available{Style.RESET_ALL}")
            time.sleep(2)
            self.run()
        except Exception as e:
            print(f"{Fore.RED}[!] Error loading SS7 module: {e}{Style.RESET_ALL}")
            time.sleep(2)
            self.run()
    
    def handle_gtp_module(self):
        """Handle GTP module selection"""
        print(f"\n{Fore.GREEN}[*] Loading GTP Module...{Style.RESET_ALL}")
        time.sleep(1)
        
        try:
            from gtpmain import prep
            prep()
        except ImportError:
            print(f"{Fore.RED}[!] GTP module not available{Style.RESET_ALL}")
            time.sleep(2)
            self.run()
        except Exception as e:
            print(f"{Fore.RED}[!] Error loading GTP module: {e}{Style.RESET_ALL}")
            time.sleep(2)
            self.run()
    
    def handle_diameter_module(self):
        """Handle Diameter module selection"""
        print(f"\n{Fore.YELLOW}[*] Diameter module will be available in version 3 release{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Returning to main menu...{Style.RESET_ALL}")
        time.sleep(3)
        self.run()
    
    def handle_sip_module(self):
        """Handle SIP module selection"""
        print(f"\n{Fore.YELLOW}[*] SIP module will be available in version 4 release{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Returning to main menu...{Style.RESET_ALL}")
        time.sleep(3)
        self.run()
    
    def exit_application(self):
        """Exit SigPloit gracefully"""
        print(f"\n{Fore.YELLOW}[*] Exiting SigPloit...{Style.RESET_ALL}")
        time.sleep(1)
        self.running = False
        sys.exit(0)
    
    def get_user_choice(self):
        """Get user input with prompt"""
        try:
            choice = input(f"\n{Fore.BLUE}sigploit>{Style.RESET_ALL} ").strip().lower()
            return choice
        except (EOFError, KeyboardInterrupt):
            return 'q'
    
    def process_choice(self, choice):
        """Process user menu choice"""
        choice_map = {
            '0': self.handle_ss7_module,
            '1': self.handle_gtp_module,
            '2': self.handle_diameter_module,
            '3': self.handle_sip_module,
            'q': self.exit_application,
            'quit': self.exit_application,
            'exit': self.exit_application
        }
        
        if choice in choice_map:
            choice_map[choice]()
        else:
            print(f"\n{Fore.RED}[!] Invalid choice. Please select 0-3 or 'q' to quit.{Style.RESET_ALL}")
            time.sleep(2)
            self.run()
    
    def run(self):
        """Main application loop"""
        while self.running:
            try:
                self.clear_screen()
                self.display_banner()
                self.display_contributors()
                self.display_main_menu()
                
                choice = self.get_user_choice()
                self.process_choice(choice)
                
            except KeyboardInterrupt:
                self.exit_application()
            except Exception as e:
                print(f"\n{Fore.RED}[!] Unexpected error: {e}{Style.RESET_ALL}")
                time.sleep(3)
                continue

def signal_handler(signal, frame):
    """Handle interrupt signals"""
    print(f"\n{Fore.YELLOW}[*] Interrupt received. Exiting...{Style.RESET_ALL}")
    time.sleep(1)
    sys.exit(0)

def main():
    """Main entry point"""
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    
    # Create and run application
    app = SigPloit()
    app.run()

if __name__ == '__main__':
    main()
