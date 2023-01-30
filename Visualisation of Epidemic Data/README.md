# Visualisation of Epidemic Data

## Overview

Within the `Infection_Datafiles` directory are `.csv` files each containing a sample of four DSTL/PHE 
supercomputer simulation results of an airborne disease outbreak over Manchester, England. Each simulation differs in 
initial conditions through varying the wind velocity, although the four-simulation groupings are generally similar in
these initial conditions. The simulations are each modelled 
by a grid of cells with corresponding longitudes and latitudes, alongside their populations and resulting infection 
counts. Each datafile, i.e. grouping of four simulations, then has several uncertainty measures that aggregate each cell
of the four simulations in some way, e.g. their infection count mean. Any cell that has zero infections in each of the
four simulations within a datafile is excluded from that file.
All the simulations have infection origin 'longitude: -2.2807386, latitude: 53.4034207'.

The two Power BI dashboards employ visualisation techniques to display the results of these simulations. 
`Visualisation Dashboard - One Datafile.pbix` visualises only one datafile, specifically `Datafile_095.csv`, whereas
`Visualisation Dashboard - All Datafiles.pbix` visualises all the datafiles. The goal of
the dashboards is to communicate where response would be ideally placed to deal with a disease outbreak in this area.

## Justification of Dashboard Content

Below is an explanation of why the dashboards were constructed the way they are.

### `Visualisation Dashboard - One Datafile.pbix` 

#### Communication of areas most and least in need of aid

The dashboard primarily features a map containing bubbles for each cell that 
can be adjusted with four slicers, each for a parameter of interest. The colour of 
the bubbles corresponds to infection count, with darker areas more affected.

Use of the slicers allows us to individually and jointly see areas of high 
infection count and uncertainty, and areas of high population count and given 
distances to the infection origin. Areas of the bar plots can also be selected to 
view these ranges using map bubbles. In doing so, we see that the areas of high 
infection count and uncertainty are concentrated around the infection origin,
decreasing the further away a cell is from this origin. There also seems to be 
some correlation between population and infection count or uncertainty, 
although this is less pronounced than with the distance to the origin.

The conclusions derived from the map are also reflected in the bar plots on 
the dashboard. We see larger values of infection count and uncertainty with 
smaller values of distance from origin, in the blue bar plots. There appears to be 
a cluster of large uncertainty values around 5.5 – 9 km from the origin. By 
looking at the yellow bar plot, we can identify that these uncertainties seem to 
be in areas of high population count, meaning that population count does seem 
to have some effect on uncertainty. Looking at the orange plots, the infection 
count and uncertainty seems to slowly increase with population count, up to a 
population count of around 160, afterwards the count and uncertainty values 
behave erratically with a slight upward trend, hinting that some other factor is 
dominating the behaviour of the infection count and uncertainty beyond this 
point; our evidence so far shows that this factor is likely to be the distance from 
the origin. The additional yellow plot of population count vs distance from 
origin serves as a secondary aid, such as in the case before to identify the 
unusual cluster of uncertainty values.

There is a ‘Key Influencers’ visual to give more specific information about 
how the infection count is influenced by distance from origin and population 
count, mostly to confirm what we have already seen in the map and bar plot 
visuals. It plainly states that the most prominent factor in increasing infection 
count is being close to the infection origin, specifically a distance of 2.803 km or 
less. Beyond this distance, increasing population count and decreasing distance 
from origin seem to have a similar effect to each other on the infection count, 
but to a much lesser degree than being within 2.803 km of the origin.

_All the information given by the dashboard leads to the same conclusion for 
the aid response: aid should be prioritised to areas within roughly 2.8 km of the 
infections point of origin. At a distance greater than that, areas with a 
combination of high population counts and close to medium distance to the 
origin should be prioritised secondarily._

#### Use of visual channels

As the data is dependent on latitude and longitude, a map is used to 
represent the cells geographically which, when combined with the slicers and 
ability to select ranges of columns in the bar plots, allows the user to observe 
where infection impact and uncertainty is at its most serious, as well as 
population counts and to visualise the distance more easily from the origin of 
infection. This can assist with seeing relationships between the variables by 
looking for similarities in the resulting bubble patterns when conditions on the 
variables are applied.

Bar plots are used to see one to one interactions between the variables. Bar 
plots were used in this dashboard to plot the impact and uncertainty against 
the distance to origin and population count, which made seeing any trend 
between them clear. A secondary plot was used to compare the explanatory 
variables to see if they correlated with each other, which would cause issues. 
Bar plots were exclusively chosen, as opposed to a combination of different 
plot types, to allow easier comparisons between plots since the user doesn’t 
have to account for how different visualisation types represent data differently.

A ’Key Influencers’ visualisation is used to state the most crucial factors 
affecting the infection count. Each factor has a diagram featuring an arrow that 
is larger the stronger a factor it is. This is mostly used to summarise the 
information we derive from the map and bar plots.

#### Use of Gestalt design principles

[1] The bar charts make use of the ‘Law of Similarity’ through being grouped 
by colour corresponding to the type of relationship they are comparing, with 
yellow comparing covariates, orange comparing infection variables against 
population count, and blue comparing infection variables against distance from 
infection origin. Each bar chart is positioned with sufficient whitespace 
between them, clearly illustrating that they are separate, making use of the 
‘Law of Proximity’. They also utilise this law in a different way by having 
identically coloured bar charts positioned next to each other.

The map makes use of ‘The Law of Similarity’ since the bubbles
corresponding to areas of low infection count, and thus low concern, are a 
distinctly different colour (a lighter blue hue) to the bubbles associated with 
high infection count. The ‘Law of closure’ is additionally utilised by the bubbles 
since the cluster of bubbles on the map can be viewed as a continuous 
spectrum of colour that propagates out from the infection origin. The density of 
the bubbles also gives rise to the ‘Law of Continuity’ with similar effect. Both
properties are useful since the infections per cell are highly dependent on 
distance from the origin point.

#### Use of colour

The bubbles in the map visualisations use a colour gradient featuring blue 
hues, and the bar plots use blue, yellow, and orange hues. This palette was 
chosen to assist primarily with colourblind users [2], being well suited to red, 
green, and blue colour blindness types [3].

The bar plots and bubbles all use colour gradients that vary enough to allow 
the user to easily distinguish between lighter (lower concern) and darker 
(higher concern) values.

The bubbles feature outlines that contrast with their centres, and the lightest 
colours in the bar plots are dark enough to be contrasted with the white 
background, to assist with viewing the dashboard in a colourless setting, e.g., 
printed to black and white.

Due to the dominance of low infection count cells, the map bubbles use an 
exponential colour gradient instead of a linear one to give more weighting, in 
terms of colour, to cells with moderate infection count.

#### Use of user interaction

Slicers are used to adjust the four parameters of interest: average infections, 
uncertainty in infections, population count and distance from origin. Adjusting 
these sliders allows the user to see on the map where chosen parameter ranges 
can be found. Additionally, by CTRL clicking and dragging on the bar plots, 
ranges can be directly chosen on the bar plots for display on the map.

The ’Key Influencers’ visualisation can be toggled between viewing the
influences of increasing or decreasing infection count. Influences can be chosen
to see how different ranges in them affect the infection count.

#### Use of language and text

The slicers use understandable terms for less statistically informed users:
infection impact, infection uncertainty, population count, and distance from
origin. Where applicable, the sliders have a technical subheading for users who 
are familiar with statistical techniques.

A card visual is used to display the number of cells visible on the map at any 
one time. This allows the user to easily perceive how many cells they are 
looking at since the brain can only distinguish roughly 4 distinct objects without 
directly counting them [4].

The bar plots use titles that clearly highlight what the bar plot is showing, 
using easy to understand terminology.

The distances between data points were approximated using a Euclidean 
distance metric, then converted to kilometres, an easily interpretable unit of 
distance for a general user.

The ‘Key Influencers’ visual provides a summary of the most prominent 
factors affecting infection count, using full sentences for ease of readability

#### Technical aspects

The full dashboard fits onto one page, so it is easy to present as a complete 
unit. The display resolution for the dashboard is 1280x720, ensuring it can 
be viewed on most desktop screens without loss of quality or formatting [5].

### `Visualisation Dashboard - All Datafiles.pbix` 

This dashboard also utilises the techniques described above, in addition to the following:

#### Communication of areas most and least in need of aid

This dashboard is largely alike the previous, with a few key 
differences. A card Is used to show the minimum and maximum values for 
variables that change between datasets, so the user knows which ranges of 
values are applicable with use of the slicers. A line plot is used to allow the user 
to see the total infection count and uncertainty for each dataset, to examine 
datasets of different epidemic scales (if no value is selected, then every dataset 
will be visualised at once). Selecting a value on the line plot makes the rest of 
the visuals on the dashboard take values only from that dataset, so they can 
infer properties for that simulation grouping. A card is used to state which dataset is 
selected. To accommodate space for these new visuals, the ‘cells visible on 
map’ and ‘key influencers’ visuals have been shrunk, which does impact the 
readability of the ‘key influencers’ visual, although the information contained 
within it can still be viewed.

_Through viewing multiple datasets individually, using the visualisations in the 
same way as the previous dashboard, a similar conclusion is reached; aid should be prioritised 
closely to the infection origin within a dataset dependent critical value, then at a 
distance greater than that, areas with a combination of high population count 
and close to medium distance to the origin should be prioritised secondarily._

#### Visualisation of multiple datasets

The full selection of 250 datasets was used to allow for the maximum 
possible sample size. This makes it easier to see behaviours describing the 
underlying process behind the data by ensuring our sample is large enough to 
describe the population as a whole [6].

All the datasets can be combined and viewed on the visualisations at once if 
desired, making it easy to see commonly shared values across datasets. 

The line plot allows you to see the overall infection impact and uncertainty 
for each dataset by summing all the infection counts and standard deviations
for each, giving a simple metric to describe, briefly, a large array of datasets.

Each dataset, after being viewed in summary, can be selected on the line plot 
to view more detailed metrics associated with it through use of the map and 
bar plots in the same way as the previous dashboard.

Large quantities of datasets can have conclusions drawn from them quickly 
by, in turn, selecting them on the line plot, viewing the ‘Key Influencers’ visual 
to see the key factors in driving infection counts, then selecting the next, 
repeated for as many datasets as the user wishes.

### References

- [1] Miklos Philips, ”How to use powerful Gestalt principles in design (with infographic)”, 2018, 
https://uxdesign.cc/how-to-use-powerful-gestalt-principles-in-design-with-infographic-4a10772eadbb
- [2] “Colour vision deficiency (colour blindness)”, 2019, NHS, 
https://www.nhs.uk/conditions/colour-vision-deficiency/
- [3] Lisa Charlotte Muth, “What to consider when visualizing data for colorblind readers”, 2020, 
https://blog.datawrapper.de/colorblindness-part2/
- [4] W. Stanley Jevons, “The Power of Numerical Discrimination”, 1871, doi: 10.1038/003281a0, Nature, Pages 281 – 282, ISSN 1476-4687, 
https://www.nature.com/articles/003281a0
- [5] “Desktop Screen Resolution Stats Worldwide”, 2022, StatCounter, 
https://gs.statcounter.com/screen-resolution-stats/desktop/worldwide
- [6] Lance P, Hattori A, “Sampling and Evaluation – A Guide to Sampling for Program Impact Evaluation”, 2016, Pages 5 – 10, 
https://www.measureevaluation.org/resources/publications/ms-16-112.html