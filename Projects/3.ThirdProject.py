class LicensePlate:
    def __init__(self, plate_id, register_date, owner): 
        self.plate_id = plate_id
        self.register_date = register_date
        self.owner = owner

    def __str__(self):
        return f"{self.plate_id} registered to {self.owner} on {self.register_date}"
    

class LicensePlateRepository:
    def __init__(self): 
        self.plates = {}

    def add_plate(self, plate): 
        self.plates[plate.plate_id] = plate

    def get_plate(self, plate_id): 
        return self.plates.get(plate_id)

    def update_plate(self, plate_id, **kwargs): 
        if plate_id in self.plates:
            for key, value in kwargs.items(): 
                setattr(self.plates[plate_id], key, value)
        else:
            raise Exception("Plate ID not found")
    
    def delete_plate(self, plate_id): 
        if plate_id in self.plates:
            del self.plates[plate_id] 
        else:
            raise Exception("Plate ID not found")
        

class RecognitionLog:
    def __init__(self): 
        self.recognitions = []

    def log_recognition(self, recognition_id, plate_id): 
        self.recognitions.append((recognition_id, plate_id))

    def get_recognition(self, recognition_id):
        return next((rec for rec in self.recognitions if rec[0] == recognition_id), None)
    
    def recognize_license_plates(plate_id, repository):
        plate = repository.get_plate(plate_id) 
        if plate:
            return plate 
        else:
            return "Plate not recognized"

    def log_recognitions(log, recognition_id, plate_id): 
        log.log_recognition(recognition_id, plate_id)


import unittest
class TestALPRSystem(unittest.TestCase): 
    def test_license_plate_operations(self):
        repo = LicensePlateRepository()
        plate = LicensePlate("XYZ123", "2023-05-01", "John Doe")
        repo.add_plate(plate)
        self.assertIn("XYZ123", repo.plates)
        self.assertEqual(repo.get_plate("XYZ123"), plate)

        repo.update_plate("XYZ123", owner="Jane Doe") 
        self.assertEqual(repo.get_plate("XYZ123").owner, "Jane Doe")
        
        repo.delete_plate("XYZ123")
        self.assertNotIn("XYZ123", repo.plates)

    def test_recognitions_logging(self):
        log = RecognitionLog()
        log.log_recognition("1", "XYZ123") 
        self.assertEqual(log.get_recognition("1"), ("1", "XYZ123"))

if __name__ == "__main__": 
    unittest.main()


