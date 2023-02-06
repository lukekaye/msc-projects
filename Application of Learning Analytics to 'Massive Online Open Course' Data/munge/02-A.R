## preprocessing for secondary analysis

# clone preprocessed data frame from previous analysis and process further
model_data = demographic_step_activity %>%
  # drop unwanted columns
  select(learner_id, age_range, highest_education_level, employment_status,
         module_number_list, module_number_list_length) %>%
  # drop rows containing 'Unknown' values in one or more columns
  filter(age_range != 'Unknown' & highest_education_level != 'Unknown' & 
           employment_status != 'Unknown')

# cache the final preprocessed data frame
cache('model_data')