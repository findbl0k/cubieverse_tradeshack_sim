# Cubieverse Trade Shack Simulator

## Overview
The Cubieverse Trade Shack Simulator is a tool designed to simulate resource drops and calculate expected values in the Cubieverse game. This simulator provides an approximation of the most efficient cubies to staff in the trade shack based on current market values and resource drop probabilities.

## Features
- **Resource Drop Simulation:** Simulates the likelihood of resource drops from cubies staffing the trade shack.
- **Market Value Integration:** Incorporates current market values to estimate the potential return from each cubie.
- **Extensive Simulation:** Conducts simulations over 10 million iterations for accurate estimations.
- **Customizability:** Allows users to update resource values as the market fluctuates.

## Installation

1. Clone the repository
2. Run the script. Ensure you have python with pandas installed

## Usage

1. Update `resources.csv` with the latest market values. Optionally, update `cubies.csv` with the latest new cubies (I won't be maintaining it)
2. Run the simulator: python simulator.py

## Notes

- **Market Fees:** The simulator does not account for market fees. Subtract these manually for a more accurate estimate.
- **Market Fluctuations:** The values in `resources.csv` are estimates. Please update them as the market changes and consider submitting a pull request with updated values.
- **Simulation Variance:** While 10 million simulations provide a solid baseline, there is noticeable variance in the expected trade shack value per visit (especially with chromatic cubies). The output may vary based on the number of visits and luck.
- **Level Assumption:** The current version assumes a level 10 cubie has a 2% chance of a drop. This will hopefully be updated as more accurate data becomes available. If you have a lower level cubie, expect a lower return.

## Contributing

Any contributions and updates from the community are greatly appreciated. If you have updates or improvements, please fork the repository, make your changes, and submit a pull request.
Donations: ltc1q4eqk8fa7l06c0f0tf935pt6phlr3pz5wvr85cd

