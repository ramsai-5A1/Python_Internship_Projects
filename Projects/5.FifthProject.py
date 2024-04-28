class Crime:
    def __init__(self, crime_id, type, description, location):
        self.crime_id = crime_id
        self.type = type
        self.description = description
        self.location = location 

    def __str__(self):
        return f"CrimeID: {self.crime_id}, Type: {self.type}, Location: {self.location}"
    
class CrimeMap:
    def __init__(self):
        self.crimes = {} 

    def add_crime(self, crime):
        if crime.crime_id in self.crimes:
            raise ValueError("Crime ID already exists") 
        self.crimes[crime.crime_id] = crime

    def read_crime(self, crime_id):
        return self.crimes.get(crime_id, None)
    

    def update_crime(self, crime):
        if crime.crime_id not in self.crimes:
            raise ValueError("Crime ID does not exist") 
        self.crimes[crime.crime_id] = crime

    def delete_crime(self, crime_id):
        if crime_id not in self.crimes:
            raise ValueError("Crime ID does not exist")
        del self.crimes[crime_id]

    def map_crime_locations(self): 
        for crime in self.crimes.values():
            print(f"Crime ID {crime.crime_id} at location {crime.location}")

    def analyze_crime_patterns(self):
        pattern_count = {}
        for crime in self.crimes.values():
            if crime.type in pattern_count: 
                pattern_count[crime.type] += 1
            else:
                pattern_count[crime.type] = 1
        return pattern_count
    
import unittest
class TestCrimeMap(unittest.TestCase): 
    def setUp(self):
        self.map = CrimeMap()
        self.map.add_crime(Crime('001', 'Theft', 'Stolen bike', (10, 10))) 
        self.map.add_crime(Crime('002', 'Assault', 'Assault in park', (20, 20)))


    def test_add_crime_existing_id(self): 
        with self.assertRaises(ValueError):
            self.map.add_crime(Crime('001', 'Burglary', 'Store burglary', (15, 15)))


    def test_delete_crime(self): 
        self.map.delete_crime('001') 
        self.assertIsNone(self.map.read_crime('001'))

    def test_analyze_patterns(self):
        patterns = self.map.analyze_crime_patterns() 
        self.assertEqual(patterns['Theft'], 1) 
        self.assertEqual(patterns['Assault'], 1)

if __name__ == "__main__": 
    unittest.main()



