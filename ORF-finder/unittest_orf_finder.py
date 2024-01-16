import unittest
from pathlib import Path
from ORF_finder import ORFFinder

empty_file_path = Path("test_data/empty_file.txt")
no_file_path = Path("test_data/no_file.txt")
integration_path = Path("test_data/integration_file.txt")
integration_output = Path("test_data/integration_output.txt")

class TestORFFinder(unittest.TestCase):
       
    def test_read_sequence(self):
        # Test if empty files are recognized
        with self.assertRaises(FileNotFoundError):
            tester = ORFFinder(input_path=empty_file_path)
            tester.read_sequence()
        # Test if no files are catched
        with self.assertRaises(FileNotFoundError):
            tester = ORFFinder(input_path=no_file_path)
            tester.read_sequence()
    
    def test_transform_sequence(self):
        tester = ORFFinder()
        tester.raw_sequence = "ccgctgccctggcgccgctgggcggcggtg"
        exspected_seq = "caccgccgcccagcggcgccagggcagcgg"
        result = tester.rev_complement
        self.assertEqual(result, exspected_seq)
    
    def test_generate_reading_frames(self):
        tester = ORFFinder()
        # Test if reading frames are correct and equal for forward and reverse
        tester.raw_sequence = "ccgctgccctggcgccgctgggcggcggtg"
        tester.rev_complement = tester.raw_sequence
        tester.generate_reading_frames()
        sequences = tester.sequences
        # Check if sequences are equal
        self.assertEqual(sequences["for_1"], sequences["rev_1"])
        self.assertEqual(sequences["for_2"], sequences["rev_2"])
        self.assertEqual(sequences["for_3"], sequences["rev_3"])
    
    def test_find_start(self):
        tester = ORFFinder()
        tester.raw_sequence = "ATGA"
        tester.transform_sequence()
        tester.generate_reading_frames()
        tester.find_start()
        found_starts = []
        for item in tester.start_dictionary.values():
            found_starts.append(*item)
        self.assertEqual(len(found_starts), 1)
    
    def test_find_stop(self):
        tester = ORFFinder()
        tester.raw_sequence = "TAGTGATAA"
        tester.transform_sequence()
        tester.generate_reading_frames()
        tester.find_stop()
        found_stops = []
        for item in tester.stop_dictionary.values():
            found_stops.append(*item)
        
        self.assertEqual(len(found_stops), 3)
    
    def test_intergation(self):
        # Test whole functionality
        exspected_lines = ["MLLGSFRLIPKETLIQVAGSSPCNLS", "M", "MGMTPRLGLESLLE", "MTPRLGLESLLE"]
        tester = ORFFinder(input_path=integration_path, output_path=integration_output)
        tester.read_sequence()
        tester.transform_sequence()
        tester.generate_reading_frames()
        tester.find_start()
        tester.find_stop()
        tester.find_orf()
        tester.translate_orf()
        tester.remove_duplicates()
        tester.write_result()
        
        with open(integration_output, "r") as file:
            for line in file:
                line.strip()
                self.assertIn(line, exspected_lines)
            

if __name__ == "__main__":
    unittest.main()
    print("Passed")
        