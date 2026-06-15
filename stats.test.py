import unittest
import math
import stats as statistics


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computed_temperature_stats = statistics.calculateStats([98.6, 98.2, 97.8, 102.2])
    epsilon = 0.001
    self.assertAlmostEqual(computed_temperature_stats["avg"], 99.2, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["max"], 102.2, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["min"], 97.8, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computed_temperature_stats = statistics.calculateStats([])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Specify the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html
    self.assertTrue(math.isnan(computed_temperature_stats["avg"]))
    self.assertTrue(math.isnan(computed_temperature_stats["max"]))
    self.assertTrue(math.isnan(computed_temperature_stats["min"]))

  def test_single_sensor_reading_returns_same_min_max_avg(self):
    computed_temperature_stats = statistics.calculateStats([98.6])
    self.assertEqual(computed_temperature_stats["avg"], 98.6)
    self.assertEqual(computed_temperature_stats["max"], 98.6)
    self.assertEqual(computed_temperature_stats["min"], 98.6)

  def test_identical_sensor_readings(self):
    computed_temperature_stats = statistics.calculateStats([100.0, 100.0, 100.0, 100.0])
    self.assertEqual(computed_temperature_stats["avg"], 100.0)
    self.assertEqual(computed_temperature_stats["max"], 100.0)
    self.assertEqual(computed_temperature_stats["min"], 100.0)

  def test_negative_temperature_values_are_handled(self):
    computed_temperature_stats = statistics.calculateStats([-10.0, -20.0, -5.0])
    epsilon = 0.001
    self.assertAlmostEqual(computed_temperature_stats["avg"], -11.6666666667, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["max"], -5.0, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["min"], -20.0, delta=epsilon)

  def test_mixed_sensor_readings_include_anomalous_negative_value(self):
    computed_temperature_stats = statistics.calculateStats([98.6, 99.1, -40.0, 100.4])
    epsilon = 0.001
    self.assertAlmostEqual(computed_temperature_stats["avg"], 64.525, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["max"], 100.4, delta=epsilon)
    self.assertAlmostEqual(computed_temperature_stats["min"], -40.0, delta=epsilon)


if __name__ == "__main__":
  unittest.main()
