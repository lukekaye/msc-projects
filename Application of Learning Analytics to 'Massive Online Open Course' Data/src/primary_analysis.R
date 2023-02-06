library('ProjectTemplate')
load.project()


# bar plot sets of count vs individual predictors


# count vs gender, excluding 'Unknown'
c_vs_gen = ggplot(data =
                    demographic_step_activity %>%
                    filter(gender != 'Unknown'),
                  mapping = aes(x = gender)) +
  geom_bar() +
  labs(title = 'Count vs Gender')

# count vs country, excluding 'Unknown'
c_vs_cou = ggplot(data =
                    demographic_step_activity %>%
                    filter(country != 'Unknown'),
                  mapping = aes(x = country)) +
  geom_bar() +
  theme(axis.text.x = element_blank(), axis.ticks.x = ) + 
  labs(title = 'Count vs Country')

# count vs age_range, ordered, excluding 'Unknown'
c_vs_age = ggplot(data = 
                   demographic_step_activity %>%
                   mutate(age_range = factor(age_range, levels =  c('<18', 
                                                                    '18-25', 
                                                                    '26-35', 
                                                                    '36-45', 
                                                                    '46-55', 
                                                                    '56-65', 
                                                                    '>65'))) %>%
                   arrange(age_range) %>%
                   filter(age_range != 'Unknown'), 
                 mapping = aes(x = age_range)) +
  geom_bar() + 
  labs(title = 'Count vs Age Range')

# count vs highest education level, excluding 'Unknown'
c_vs_hig = ggplot(data =
                    demographic_step_activity %>%
                    mutate(highest_education_level = factor(highest_education_level, levels =  c('less_than_secondary', 
                                                                                   'secondary', 
                                                                                   'tertiary', 
                                                                                   'university_degree', 
                                                                                   'university_masters', 
                                                                                   'university_doctorate', 
                                                                                   'apprenticeship',
                                                                                   'professional'))) %>%
                    arrange(highest_education_level) %>%
                    filter(highest_education_level != 'Unknown'),
                  mapping = aes(x = highest_education_level)) +
  geom_bar() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = 'Count vs Highest Education Level')

# count vs employment status, excluding 'Unknown'
c_vs_emps = ggplot(data =
                    demographic_step_activity %>%
                    mutate(employment_status = factor(employment_status, levels =  c('not_working', 
                                                                                            'unemployed', 
                                                                                            'retired', 
                                                                                            'full_time_student', 
                                                                                            'looking_for_work', 
                                                                                            'self_employed', 
                                                                                            'working_part_time',
                                                                                            'working_full_time'))) %>%
                    arrange(employment_status) %>%
                    filter(employment_status != 'Unknown'),
                  mapping = aes(x = employment_status)) +
  geom_bar() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = 'Count vs Employment Status')

# count vs employment area, excluding 'Unknown'
c_vs_empa = ggplot(data =
                    demographic_step_activity %>%
                    filter(employment_area != 'Unknown'),
                  mapping = aes(x = employment_area)) +
  geom_bar() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = 'Count vs Employment Area')



# get names of 5 most common countries accessing the course
top_5_countries = demographic_step_activity %>%
  count(country) %>%
  arrange(desc(n)) %>%
  slice(1:5)

# count of learners from top 10 countries by learner count
top_10_countries_count = demographic_step_activity %>%
  count(country) %>%
  arrange(desc(n)) %>%
  slice(1:10) %>%
  summarise(sum(n))
# proportion of learners from top 10 countries by learner count
top_10_countries_prop = as.numeric(top_10_countries_count)/as.numeric(demographic_step_activity %>%
                                                                      count(country) %>%
                                                                      summarise(sum(n)))

# bar plots of module_number_list_length vs predictors


# accessed module count vs gender, excluding 'Unknown', with quartiles
modules_gender = ggplot(data = 
                          demographic_step_activity %>%
                          filter(gender != 'Unknown'),
                        mapping = aes(x = gender, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ gender, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(legend.position="none") + 
  labs(title = 'Accessed Module Count vs Gender')

# accessed module count vs country, excluding 'Unknown', with quartiles
modules_country = ggplot(data = 
                           demographic_step_activity %>%
                           filter(country != 'Unknown') %>%
                           filter(country == 'GB' | country == 'IN' | country
                                  == 'US' | country == 'NG' | country == 'AU' |
                                    country == 'IT' | country == 'MX' | country
                                  == 'SA' | country == 'PK' | country == 'ZA'),
                         mapping = aes(x = country, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ country, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(legend.position="none") + 
  labs(title = 'Accessed Module Count vs Country')

# accessed module count vs age, ordered, excluding 'Unknown', with quartiles
modules_age = ggplot(data = 
                       demographic_step_activity %>%
                       mutate(age_range = factor(age_range, levels =  c('<18', 
                                                                        '18-25', 
                                                                        '26-35', 
                                                                        '36-45', 
                                                                        '46-55', 
                                                                        '56-65', 
                                                                        '>65'))) %>%
                       arrange(age_range) %>%
                       filter(age_range != 'Unknown'),
                        mapping = aes(x = age_range, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ age_range, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(legend.position="none") + 
  labs(title = 'Accessed Module Count vs Age')

# accessed module count vs education, excluding 'Unknown', with quartiles
modules_education = ggplot(data =
                       demographic_step_activity %>%
                       mutate(highest_education_level = factor(highest_education_level, levels =  c('less_than_secondary', 
                                                                                                    'secondary', 
                                                                                                    'tertiary', 
                                                                                                    'university_degree', 
                                                                                                    'university_masters', 
                                                                                                    'university_doctorate', 
                                                                                                    'apprenticeship',
                                                                                                    'professional'))) %>%
                       arrange(highest_education_level) %>%
                       filter(highest_education_level != 'Unknown'),
                     mapping = aes(x = highest_education_level, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ highest_education_level, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
        legend.position = 'none') +
  labs(title = 'Accessed Module Count vs Education')

# accessed module count vs employment status, excluding 'Unknown', with quartiles
modules_status = ggplot(data =
                             demographic_step_activity %>%
                             mutate(employment_status = factor(employment_status, levels =  c('not_working', 
                                                                                              'unemployed', 
                                                                                              'retired', 
                                                                                              'full_time_student', 
                                                                                              'looking_for_work', 
                                                                                              'self_employed', 
                                                                                              'working_part_time',
                                                                                              'working_full_time'))) %>%
                             arrange(employment_status) %>%
                             filter(employment_status != 'Unknown'),
                           mapping = aes(x = employment_status, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ employment_status, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
        legend.position = 'none') +
  labs(title = 'Accessed Module Count vs Status')

# accessed module count vs employment area, excluding 'Unknown', with quartiles
modules_area = ggplot(data =
                          demographic_step_activity %>%
                          filter(employment_area != 'Unknown'),
                        mapping = aes(x = employment_area, y = module_number_list_length)) +
  geom_jitter() +
  facet_grid(~ employment_area, scales = 'free') +
  stat_summary(fun = "quantile", fun.args = list(probs = c(0.25,0.5,0.75)), 
               geom = "hline", aes(yintercept = ..y.., colour = 'red')) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
        legend.position = 'none') +
  labs(title = 'Accessed Module Count vs Employment Area')
