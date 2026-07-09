# Changelog

## v0.1.0 - Project Initialization
- Created project structure
- Configured Git and GitHub
- Loaded Bengaluru House Price dataset

## v0.2.0 - Data Cleaning
- Removed `society` column
- Converted `total_sqft`
- Removed invalid entries
- Handled missing values
- Created `bhk` feature
- Removed duplicate records

## v0.3.0 - Feature Engineering
- Added `price_per_sqft`
- Added `sqft_per_bhk`
- Removed unrealistic houses (`sqft_per_bhk < 300`)