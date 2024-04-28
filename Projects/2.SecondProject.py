class DispatchRecord:
    def __init__(self, dispatch_id, incident_details):
        self.dispatch_id = dispatch_id
        self.incident_details = incident_details 
        self.response_start_time = None 
        self.response_end_time = None
    
    def log_response_start(self, start_time):
        self.response_start_time = start_time

    def log_response_end(self, end_time):
        self.response_end_time = end_time

    def get_response_time(self):
        if self.response_start_time and self.response_end_time:
            return self.response_end_time - self.response_start_time 
        return None
    
class DispatchManager: 
    def __init__(self):
        self.dispatches = {}

    def create_dispatch(self, dispatch_id, incident_details): 
        if dispatch_id in self.dispatches:
            raise ValueError(f"Dispatch ID {dispatch_id} already exists.") 
        self.dispatches[dispatch_id] = DispatchRecord(dispatch_id, incident_details)

    def read_dispatch(self, dispatch_id):
        return self.dispatches.get(dispatch_id)
    
    def update_dispatch(self, dispatch_id, new_details):
        if dispatch_id in self.dispatches:
            self.dispatches[dispatch_id].incident_details = new_details 
        else:
            raise KeyError(f"Dispatch ID {dispatch_id} not found.")

    def delete_dispatch(self, dispatch_id): 
        if dispatch_id in self.dispatches:
            del self.dispatches[dispatch_id] 
        else:
            raise KeyError(f"Dispatch ID {dispatch_id} not found.")
        

class ResponseTimeTracker: 
    def __init__(self):
        self.response_times = []

    def add_response_time(self, time):
        self.response_times.append(time)

    def average_response_time(self):
        if not self.response_times:
            return 0
        return sum(self.response_times) / len(self.response_times)
    


import unittest
class TestPoliceDispatchSystem(unittest.TestCase): 
    def test_dispatch_creation(self):
        dm = DispatchManager() 
        dm.create_dispatch(101, "Robbery in progress") 
        self.assertIn(101, dm.dispatches)
    
    def test_response_time(self):
        rt = ResponseTimeTracker() 
        rt.add_response_time(300) 
        rt.add_response_time(450)
        self.assertEqual(375, rt.average_response_time())

if __name__ == '__main__': 
    unittest.main()
