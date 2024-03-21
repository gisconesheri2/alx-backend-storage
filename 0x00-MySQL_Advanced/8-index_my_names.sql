-- create an index using first letter in the name column
CREATE INDEX idx_name_first ON names (name(1));