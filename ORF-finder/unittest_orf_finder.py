import unittest
from pathlib import Path
from ORF_finder import ORFFinder

empty_file_path = Path("test_data/empty_file.txt")
no_file_path = Path("test_data/no_file.txt")
integration_path = Path("test_data/integration_file.txt")
integration_output = Path("test_data/integration_output.txt")

class TestORFFinder(unittest.TestCase):
    """Test suite for the ORFFinder class."""
       
    def test_read_sequence(self):
        """Test if the ORFFinder correctly handles empty and non-existent input files."""
        # Test if empty files are recognized
        with self.assertRaises(FileNotFoundError, msg="File not found exception should be raised"):
            tester = ORFFinder(input_path=empty_file_path)
            tester.read_sequence()
        # Test if no files are catched
        with self.assertRaises(FileNotFoundError, msg="File not found exception should be raised"):
            tester = ORFFinder(input_path=no_file_path)
            tester.read_sequence()
    
    def test_transform_sequence(self):
        """Test the transformation of a raw DNA sequence into its reverse complement."""
        tester = ORFFinder()
        tester.raw_sequence = "CCGCTGCCCTGGCGCCGCTGGGCGGCGGTG"
        expected_seq = "CACCGCCGCCCAGCGGCGCCAGGGCAGCGG"
        tester.transform_sequence()
        result = tester.rev_complement
        self.assertEqual(result, expected_seq)
    
    def test_generate_reading_frames(self):
        """Test the generation of reading frames and their equality for forward and reverse strands."""
        tester = ORFFinder()
        # Test if reading frames are correct and equal for forward and reverse
        tester.raw_sequence = "CCGCTGCCCTGGCGCCGCTGGGCGGCGGTG"
        tester.rev_complement = tester.raw_sequence
        tester.generate_reading_frames()
        sequences = tester.sequences
        # Check if sequences are equal
        self.assertEqual(sequences["for_1"], sequences["rev_1"])
        self.assertEqual(sequences["for_2"], sequences["rev_2"])
        self.assertEqual(sequences["for_3"], sequences["rev_3"])
    
    def test_find_start(self):
        """Test the identification of start codons in a DNA sequence."""
        tester = ORFFinder()
        tester.raw_sequence = "ATGA"
        tester.transform_sequence()
        tester.generate_reading_frames()
        tester.find_start()
        found_starts = 0
        for values in tester.start_dictionary.values():
            found_starts += len(values)
        self.assertEqual(found_starts, 1)
    
    def test_find_stop(self):
        """Test the identification of stop codons in a DNA sequence."""
        tester = ORFFinder()
        tester.raw_sequence = "TAGTGATAA"
        tester.transform_sequence()
        tester.generate_reading_frames()
        tester.find_stop()
        found_stops = 0
        for values in tester.stop_dictionary.values():
            found_stops += len(values)
        
        self.assertEqual(found_stops, 3)
    
    def test_intergation(self):
        """Test the complete functionality of the ORFFinder class on an input DNA sequence."""
        expected_lines = sorted(["MLLGSFRLIPKETLIQVAGSSPCNLS", "M", "MGMTPRLGLESLLE", "MTPRLGLESLLE"])
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
            actual_lines = sorted([line.strip() for line in file])
            
        self.assertListEqual(actual_lines, expected_lines, "Output lines do not match expected lines.")
            
if __name__ == "__main__":
    unittest.main()
        