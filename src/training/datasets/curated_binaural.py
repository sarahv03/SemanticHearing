from src.training.datasets.semaudio_binaural_base import SemAudioBinauralBaseDataset

class CuratedBinauralDataset(SemAudioBinauralBaseDataset):
    """
    Torch dataset object for synthetically rendered spatial data.
    """
    labels = [
            # Original 20 labels
            "alarm_clock", "baby_cry", "birds_chirping", "cat", "car_horn", 
            "cock_a_doodle_doo", "cricket", "computer_typing", 
            "dog", "glass_breaking", "gunshot", "hammer", "music", 
            "ocean", "door_knock", "singing", "siren", "speech", 
            "thunderstorm", "toilet_flush",
            # New labels from FOAMS dataset
            "artifact", "basketball_dribbling", "beeping", "chewing_gum",
            "clearing_throat", "clicking", "coffee_shop", "coughing", 
            "drumming", "exhaling", "flipping_newspaper_pages", "footsteps",
            "hairdryer", "harp", "human_breathing", "knife_cutting", 
            "laughing", "lip_smacks", "mouth_sounds_other", "plastic_crumpling",
            "recording_artifact", "sliding_ceramic", "slurping", "squishing",
            "swallowing", "talking", "tapping", "tearing_paper", "typing",
            "water_drops", "whimpering"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.labels = [
            # Original 20 labels
            "alarm_clock", "baby_cry", "birds_chirping", "cat", "car_horn", 
            "cock_a_doodle_doo", "cricket", "computer_typing", 
            "dog", "glass_breaking", "gunshot", "hammer", "music", 
            "ocean", "door_knock", "singing", "siren", "speech", 
            "thunderstorm", "toilet_flush",
            # New labels from FOAMS dataset
            "artifact", "basketball_dribbling", "beeping", "chewing_gum",
            "clearing_throat", "clicking", "coffee_shop", "coughing", 
            "drumming", "exhaling", "flipping_newspaper_pages", "footsteps",
            "hairdryer", "harp", "human_breathing", "knife_cutting", 
            "laughing", "lip_smacks", "mouth_sounds_other", "plastic_crumpling",
            "recording_artifact", "sliding_ceramic", "slurping", "squishing",
            "swallowing", "talking", "tapping", "tearing_paper", "typing",
            "water_drops", "whimpering"]
