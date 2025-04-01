"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """First manually written test case."""
        # TODO: Implement this test
        pass
    
    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.
    
    def test_ai_chronological_order(self):
        """
        AI-assisted test case that verifies concerts are returned in chronological order.
        Tests constraint #2: The itinerary should return a list of concerts sorted in 
        chronological order (by date from earliest to latest).
        """
        # Arrange
        later_concert = Concert(
            artist="Artist A",
            date="2025-04-15",
            location="Venue A"
        )
        earlier_concert = Concert(
            artist="Artist B",
            date="2025-04-01",
            location="Venue B"
        )
        
        # Act
        self.builder.add_concert(later_concert)
        self.builder.add_concert(earlier_concert)
        itinerary = self.builder.get_itinerary()
        
        # Assert
        self.assertEqual(len(itinerary), 2, "Itinerary should contain both concerts")
        self.assertEqual(itinerary[0].date, "2025-04-01", "First concert should be the earlier date")
        self.assertEqual(itinerary[1].date, "2025-04-15", "Second concert should be the later date")


if __name__ == "__main__":
    unittest.main()