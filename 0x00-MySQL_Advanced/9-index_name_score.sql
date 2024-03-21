-- create an index using first letter in the name column
-- and the score column
CREATE INDEX idx_name_first_score ON names (name(1), score);