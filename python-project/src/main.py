#!/usr/bin/env python3
"""
Main application entry point.

This is a template Python project with best practices:
- Virtual environment setup
- Proper project structure  
- Environment variables
- Type hints
- Error handling
- Logging
"""

import os
import logging
from typing import Optional
from dotenv import load_dotenv


def setup_logging() -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def get_config_value(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get configuration value from environment variables."""
    return os.getenv(key, default)


def main() -> None:
    """Main application function."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Get configuration
    app_name = get_config_value('APP_NAME', 'Python Template')
    debug_mode = get_config_value('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting {app_name}")
    logger.info(f"Debug mode: {debug_mode}")
    
    # Your application logic here
    print(f"Hello from {app_name}!")
    print("This is your Python project template.")
    
    if debug_mode:
        print("Debug mode is enabled")
    
    logger.info("Application completed successfully")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Application failed: {e}")
        exit(1)