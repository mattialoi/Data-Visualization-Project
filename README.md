SUPSI 2025-26 
Data Visualization course, C-D3202E 
Teacher Giovanni Profeta


# Project title
Authors: [Author n. 1]Anna Dell'Aquila, [Author n. 2]Antonio Falcao, [Author n. 3]Mattia Loi

[China: The Green Evolution](https://dataviz-supsi.github.io/2025/)


## Abstract
This project explores China's extraordinary agricultural transformation from 1961 to the present. Through visual analysis, we document how the nation managed to feed an exploding population without a proportional increase in land use. This phenomenon, known as the "Great Decoupling," reveals the critical role of nutrient intensification and increased agricultural yields in global food security.


## Introduction
Faced with unprecedented demographic pressure, China had to reinvent its food system. The challenge was not just to produce more food, but to do so efficiently. This data story analyzes the shift from agriculture based on territorial expansion to a technological and chemical evolution ("The Green Evolution"), highlighting how production growth has been driven by yields rather than cultivated area.


## Data sources
The data used for this analysis comes primarily from **FAOSTAT** (Food and Agriculture Organization of the United Nations), which provides accurate historical series on production, yields, and land use. Data regarding fertilizer production was extracted from international datasets monitoring nutrient input (NPK) in the soil.

[Main datasource](https://www.fao.org/faostat/en/#data/QCL): "Production_Crops_Livestock_E_All_Data/Production_Crops_Livestock_E_All_Data_NOFLAG.csv".

## Data pre-processing
The original data in .csv format were cleaned and filtered using Python (Pandas) to isolate the focus on China. 
We filtered for 'Production' (Element Code 5510) and unit 't' (tonnes). This isolates the data representing the physical quantity produced.
We excluded animal-derived items using keywords (case-insensitive). 
Then we created the 'Year' column (short format), calculated the total production (sum across all years) and grouped by Item. We calculated the total production for each record (Area/Item/Element combination) and selected the top 15 plant productions, creating a new dataset further processed to analyze China in particular (i.e. we calculated percentage changes relative to the base year (1961) to normalize the different scales of measurement between population (billions), production (tons), and area (hectares)). 

**Note**: the protocols using the FAOSTAT dataset refer to the already modified original dataset "Production_Crops_Livestock_E_All_Data/Production_Crops_Livestock_E_All_Data_NOFLAG.csv" to which we applied the modifications cited above.

## Data visualizations
- Heat World Map
- Line Chart
- Hans-Rosling Scatter Plot
- Horizontally Stacked Bar Chart
- Bar Chart Race / Line Chart

### World Population by Country
Used to highlight Chiina's population rapid growth in comparison to other countries. This, with the knowledge of how devastating the Great Chinese Famine in 1959-1961 was, is where our research question came from: "How was China able to feed its population?".
<div class="flourish-embed flourish-map" data-src="visualisation/27051099"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/27051099/thumbnail" width="100%" alt="map visualization" /></noscript></div>
  

### Global Indices Change (1961-2023)
Visual representation of area harvested, production, yield (focus on cereals) and global population.
 <div class="flourish-embed flourish-chart" data-src="visualisation/26807022"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/26807022/thumbnail" width="100%" alt="chart visualization" /></noscript></div>
 

### Correlation between Land Use and Production across major Chinese crop categories
Scatter plot that shows production (arising) oon the x axis and area harvested on the y axis. The size of the circles are proportional to the yield of each item overtime.
<div class="flourish-embed flourish-scatter" data-src="visualisation/27142656"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/27142656/thumbnail" width="100%" alt="scatter visualization" /></noscript></div>

### Production and are harvested for different crops (1961 vs 2023)
Bar charts showing change in proportion between area harvested and production. The sums on the right of each item are indicative (units are not to be taken in consideration) and are used to show the magnitudes better.
<div class="flourish-embed flourish-hierarchy" data-src="visualisation/26784114">
          <script src="https://public.flourish.studio/resources/embed.js"></script>
          <noscript><img src="https://public.flourish.studio/visualisation/26784114/thumbnail" width="100%"
                         alt="Initial stage visualization" /></noscript>
        </div>
<div class="flourish-embed flourish-hierarchy" data-src="visualisation/26788354">
          <script src="https://public.flourish.studio/resources/embed.js"></script>
          <noscript><img src="https://public.flourish.studio/visualisation/26788354/thumbnail" width="100%"
                         alt="Final stage visualization" /></noscript>
        </div>

### Fertilizer Production [tonnes] by nutrient type
Shows the rise in the usage of different types of fertilizers (K2O=potash, P2O5=phosphate, N=nitrogen).
<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/27145742"><script src="https://public.flourish.studio/resources/embed.js"></script><noscript><img src="https://public.flourish.studio/visualisation/27145742/thumbnail" width="100%" alt="bar-chart-race visualization" /></noscript></div>
 
## Key findings
- Land Efficiency: China now produces over 500% more cereals than in 1961 using almost the same amount of land.
- Nutrient Input: The production and use of NPK fertilizers have been the fundamental chemical engine for sustaining necessary yields.
- Resilience: The "decoupling" between land and food is the key to future sustainability and the protection of China's natural ecosystems.

## Next steps
In the future, the project could expand by analyzing the environmental impact of this Green Evolution, such as water eutrophication due to excess fertilizer, and China's current transition toward smart and organic agriculture to reduce its chemical footprint. It would also be interesting to analyze which crop responded better to each type of fertilizer, which would be useful for agricultural analysis and improvement.

