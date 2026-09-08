import re
from datetime import datetime
import inquirer

def validate_amount(_, current):
    try:
        val = float(current)
        if val > 0:
            return True
        raise Exception()
    except Exception:
        raise inquirer.errors.ValidationError('', reason='Please enter a valid positive number.')
    
