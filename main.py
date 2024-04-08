from abc import ABC, abstractmethod

# Define an abstract class representing the interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Define a concrete class that implements the Logger interface
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Logging to console: {message}")

# Define a NullLogger class that acts as the Null Object
class NullLogger(Logger):
    def log(self, message):
        pass  # Null operation, does nothing

# Function to create the appropriate logger based on a condition
def create_logger(verbose=True):
    if verbose:
        return ConsoleLogger()
    else:
        return NullLogger()

# Usage
logger = create_logger(verbose=False)
logger.log("This message will not be logged")  # No output

logger = create_logger(verbose=True)
logger.log("This message will be logged to console")  # Output: Logging to console: This message will be logged to console
