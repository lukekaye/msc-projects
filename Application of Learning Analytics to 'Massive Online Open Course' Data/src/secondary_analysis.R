library('ProjectTemplate')
load.project()


# test if ANOVA is appropriate

# fit full multiplicative linear model
linear_model = lm(module_number_list_length ~ 
                    age_range * highest_education_level * employment_status,
                  data = model_data)
# quantile-quantile plot
linear_model_qq = ggplot(model_data, aes(sample = module_number_list_length)) +
  stat_qq() +
  stat_qq_line()
# shapiro-wilks test in rmarkdown file


# test if poisson is appropriate

# fit full poisson model
poisson_model = glm(module_number_list_length ~ 
                      age_range + highest_education_level + employment_status, 
                    family = poisson, data = model_data)
# test for overdispersion in rmarkdown file


# test mixture models with point mass binomial and poisson parts

# fit full zi poisson model
zi_poisson_model = zeroinfl(module_number_list_length ~ 
                              age_range + highest_education_level + employment_status | 1,
                            data = model_data, dist = "poisson")
# fit full hurdle poisson model
h_poisson_model = hurdle(module_number_list_length ~ 
                           age_range + highest_education_level + employment_status | 1, 
                         data = model_data, dist = "poisson") 

# fit full zi negative binomial model
zi_negbin_model = zeroinfl(module_number_list_length ~ age_range + highest_education_level + employment_status | 1,
                 data = model_data, dist = "negbin")
# fit full hurdle negative binomial model
h_negbin_model = hurdle(module_number_list_length ~ age_range + highest_education_level + employment_status | 1, data = model_data,
              dist = "negbin")
