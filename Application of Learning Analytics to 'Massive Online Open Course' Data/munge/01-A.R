## preprocessing for primary analysis


# preprocessing specific to step-activity


# create blank tibble with required columns from data sets
step_activity_combined = 
  tibble(learner_id = character(),
         step = numeric(),
         week_number = numeric(),
         step_number = numeric(),
         first_visited_at = character(),
         last_completed_at = character())

# iterate over all 7 data sets, appending required columns to previous tibble
for(i in 1:7) {
  # get string name of current dataset
  current_dataset_string = sprintf("cyber.security.%s_step.activity", i)
  # set current dataset to be worked on based on the current set string name
  current_dataset =  eval(as.name(current_dataset_string))
  # append data to master data frame
  step_activity_combined = current_dataset %>%
    add_row(step_activity_combined)
}

# further preprocessing
step_activity_cleaned = step_activity_combined %>%
  # remove observations with step = 3.21
  filter(step != 3.21) %>%
  # remove step, first_visited_at, last_completed_at columns
  select(learner_id, week_number, step_number) %>%
  # convert module_number to ordinal number representation  
  mutate(module_number = case_when(
    week_number == 1 ~ step_number,
    week_number == 2 ~ 19 + step_number,
    week_number == 3 ~ 42 + step_number,
  )) %>%
  # delete now unused week_number and step_number
  select(learner_id, module_number) %>%
  # collapse observations on the same learner_id to one row each, with
  # module_number_list being a list of all accessed modules by that learner
  group_by(learner_id) %>%
  summarise(module_number_list = list(module_number))


# preprocessing specific to enrolment


# create blank tibble with required columns from data sets
enrolment_combined = 
  tibble(learner_id = character(),
         enrolled_at = character(),
         unenrolled_at = character(),
         role = character(),
         fully_participated_at = character(),
         purchased_statement_at = character(),
         gender = character(),
         country = character(),
         age_range = character(),
         highest_education_level = character(),
         employment_status = character(),
         employment_area = character(),
         detected_country = character())

# iterate over all 7 data sets, appending required columns to previous tibble
for(i in 1:7) {
  # get string name of current dataset
  current_dataset_string = sprintf("cyber.security.%s_enrolments", i)
  # set current dataset to be worked on based on the current set string name
  current_dataset =  eval(as.name(current_dataset_string))
  # append data to master data frame
  enrolment_combined = current_dataset %>%
    add_row(enrolment_combined)
}

# further preprocessing
enrolment_cleaned = enrolment_combined %>%
  # remove enrolled_at, unenrolled_at, fully_participated_at,
  # purchased_statement_at, detected_country columns
  select(learner_id, role, gender, country, age_range, highest_education_level,
         employment_status, employment_area) %>%
  # remove rows corresponding to non-learners
  filter(role == 'learner') %>%
  # remove role column
  select(!role) %>%
  # remove rows with all 6 demographic variables unknown
  filter(gender != 'Unknown' | country != 'Unknown' | age_range != 'Unknown' |
           highest_education_level != 'Unknown' | employment_status != 'Unknown'
          | employment_area != 'Unknown') %>%
  # remove rows with NA values
  drop_na() %>%
  # remove any rows that share a learner_id with another row
  group_by(learner_id) %>%
  filter(n() == 1) %>%
  ungroup()


# final preprocessing, combining the data into one data frame appropriately


# new tibble with combined observations of enrolment_cleaned and
# step_activity_cleaned, discarding excess observations in step_activity_cleaned
demographic_step_activity = left_join(enrolment_cleaned, step_activity_cleaned) %>%
  # replace NULL values in module_number_list with zeroes
  replace_na(list(module_number_list=list(0))) %>%
  # new column of count of entries in module_number_list
  mutate(module_number_list_length = lengths(module_number_list)) %>%
  # change rows where module_number_list == 0 to have their counts reduced by 1
  mutate(module_number_list_length = 
           replace(module_number_list_length, 
                   lapply(module_number_list, head, 1) == 0, 0))


# cache all intermediate and final preprocessed data frames
cache('step_activity_combined')
cache('step_activity_cleaned')
cache('enrolment_combined')
cache('enrolment_cleaned')
cache('demographic_step_activity')