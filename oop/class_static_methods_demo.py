class Calculator:    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: performs addition.
        Does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: performs multiplication.
        Has access to the class via 'cls' and can use class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
