import unittest
from datetime import datetime

class Checkpoint:
    def __init__(self, checkpoint_id, location, date):
        self.checkpoint_id = checkpoint_id 
        self.location = location
        self.date = date
        self.scheduled = False

    def update_location(self, new_location): 
        self.location = new_location

    def update_date(self, new_date): 
        self.date = new_date

    def __str__(self):
        return f"Checkpoint ID: {self.checkpoint_id}, Location: {self.location}, Date: {self.date}, Scheduled: {self.scheduled}"
    

class CheckpointData:
    def __init__(self, data_id, checkpoint_id, incidents_reported, outcomes):
        self.data_id = data_id
        self.checkpoint_id = checkpoint_id 
        self.incidents_reported = incidents_reported 
        self.outcomes = outcomes

    def update_incidents(self, new_incidents): 
        self.incidents_reported = new_incidents

    def update_outcomes(self, new_outcomes): 
        self.outcomes = new_outcomes

    def __str__(self):
        return f"Data ID: {self.data_id}, Checkpoint ID: {self.checkpoint_id}, Incidents: {self.incidents_reported}, Outcomes: {self.outcomes}"

class CheckpointManager:
    def __init__(self):
        self.checkpoints = {} 
        self.data_records = {}

    def add_checkpoint(self, checkpoint_id, location, date): 
        if checkpoint_id not in self.checkpoints:
            self.checkpoints[checkpoint_id] = Checkpoint(checkpoint_id, location, date) 
        else:
            raise ValueError("Checkpoint ID already exists")
        
    def update_checkpoint(self, checkpoint_id, location=None, date=None): 
        if checkpoint_id in self.checkpoints:
            if location: 
                self.checkpoints[checkpoint_id].update_location(location)
            if date: 
                self.checkpoints[checkpoint_id].update_date(date)
        else:
            raise KeyError("No such checkpoint with ID")
        

    def delete_checkpoint(self, checkpoint_id): 
        if checkpoint_id in self.checkpoints:
            del self.checkpoints[checkpoint_id]
        else:
            raise KeyError("No such checkpoint to delete")
        
    def add_checkpoint_data(self, data_id, checkpoint_id, incidents_reported, outcomes): 
        if data_id not in self.data_records:
            if checkpoint_id in self.checkpoints:
                self.data_records[data_id] = CheckpointData(data_id, checkpoint_id, incidents_reported, outcomes)
            else:
                raise KeyError("No such checkpoint to link data")
        else:
            raise ValueError("Data ID already exists")
        
    def update_checkpoint_data(self, data_id, incidents=None, outcomes=None): 
        if data_id in self.data_records:
            if incidents: 
                self.data_records[data_id].update_incidents(incidents)
            if outcomes: 
                self.data_records[data_id].update_outcomes(outcomes)
        else:
            raise KeyError("No such data record")
        
    def delete_checkpoint_data(self, data_id): 
        if data_id in self.data_records:
            del self.data_records[data_id] 
        else:
            raise KeyError("No such data record to delete")
        
    def schedule_checkpoint(self, checkpoint_id): 
        if checkpoint_id in self.checkpoints:
            self.checkpoints[checkpoint_id].scheduled = True
        else:
            raise KeyError("Checkpoint does not exist")

class TestCheckpointManager(unittest.TestCase):
    def test_add_and_schedule_checkpoint(self):
        manager = CheckpointManager() 
        manager.add_checkpoint("CP001", "LocationA", "2023-10-31") 
        manager.schedule_checkpoint("CP001") 
        self.assertTrue(manager.checkpoints["CP001"].scheduled)

    def test_update_and_delete_checkpoint_data(self):
        manager = CheckpointManager()
        manager.add_checkpoint("CP001", "LocationA", "2023-10-31") 
        manager.add_checkpoint_data("DATA001", "CP001", 3, "2 arrests, 1 warning") 
        manager.update_checkpoint_data("DATA001", incidents=4) 
        self.assertEqual(manager.data_records["DATA001"].incidents_reported, 4) 
        manager.delete_checkpoint_data("DATA001")
        self.assertNotIn("DATA001", manager.data_records)

if __name__ == '__main__': 
    unittest.main()


