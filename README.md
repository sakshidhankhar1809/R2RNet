# R2RNet: A deep spatiotemporal RaintoRiverNetwork for water level prediction and flood forecasting

This repository contains the code for the paper "R2RNet: A deep spatiotemporal RaintoRiverNetwork for water level prediction and flood forecasting".


## Introduction

This paper introduces the RaintoRiverNetwork (R2RNet), a novel approach designed to integrate radar-derived precipitation data with river water levels measured in Goslar. By capturing the dynamic nature of precipitation events, STRPM aims to improve the lead time and reliability of flood forecasts. This model addresses the limitations of limited upstream data by incorporating high-frequency radar observations, which offer detailed insights into the spatial distribution and intensity of rainfall. The primary objectives of this research are to develop and validate the R2R, assess its performance in various scenarios, and demonstrate its potential for operational flood forecasting. The model's performance is systematically evaluated using the original Goslar Benchmark: [https://www.scitepress.org/Link.aspx?doi=10.5220/0012081700003546](https://doi.org/10.1016/j.ejrh.2025.102571) together with additional experiments to assess its accuracy. To validate the model's robustness, additional testing was conducted on data from Göttingen. This validation demonstrated the model's flexibility, indicating its potential for future implementation in regions with varying topologies through the application of transfer-learning techniques.


## Abstract

***Study Region:*** Goslar and Göttingen, Lower Saxony, Germany.

***Study Focus:*** In July 2017, the cities of Goslar and Göttingen experienced severe regional flood events characterized by short warning time of only 20~min with a significant damage. This highlights the critical need for a more reliable and timely flood forecasting system. This paper presents a comprehensive study on the impact of radar-based precipitation data on forecasting river water levels in Goslar and Göttingen. The analysis integrates radar-derived spatiotemporal precipitation patterns with hydrological sensor data obtained from ground stations to evaluate the effectiveness of this approach in improving flood prediction capabilities. 

***New Hydrological Insights for the Region:*** A key innovation in this paper is the use of residual-based modeling to address the non-linearity between precipitation images and water levels, leading to a Rain2RiverNetwork with residual-corrections (R2RNet). The deep learning architecture integrates (2+1)D convolutional neural networks for spatial and temporal feature extraction with LSTM for timeseries forecasting. The results of our evaluation demonstrate the potential of R2RNet for capturing extreme events with good prediction accuracy for 4-hours ahead as Nash--Sutcliffe efficiency=0.93, Bravais--Pearson=0.98 and Index of Agreement=0.99. These results are comparable to the conventional model using upstream data for predictions, with NSE=0.95, BP=0.97 and IoA=0.98. These results quantitatively underscore the enhanced predictive capability of R2RNet, making it independent of additional hydrological upstream measurements.


## Data

This paper utilizes three datasets, one of which is the publicly available ground-based RADAR precipitation dataset from the DWD: https://opendata.dwd.de/climate_environment/CDC/grids_germany/5_minutes/radolan/reproc/2017_002/asc/, the national meteorological service of Germany. The dataset consists of Radar Online Calibration (RADOLAN) precipitation images, which are provided at a temporal resolution of 5-minute intervals and a spatial resolution of 1 km x 1 km. The selected time period for analysis spans from November 1, 2003, to June 30, 2018, covering approximately 15 years of continuous precipitation data. 

The second dataset comprises water level measurements for Goslar recorded at Sennhuette hydrological sensor station provided by Harzwasserwerke GmbH, corresponding to the same time interval. These water level measurements are captured at a temporal resolution of 15-minute intervals and serve as the target variable in our experiments for Goslar. 

The third dataset comprises water level measurements for Göttingen provided by Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz (NLWKN), corresponding to the same time interval with 15-minutes resolution. This dataset is used for validation purposes in this paper.


## Performance evaluation

The performance of this model can be evaluated using various overall metrics such as *Nash Sucliffe efficiency(NSE)*, *Index of agreement (IoA)*, *Mean squared error(MSE)* and *Bravais-Pearson (BP)*, to assess the accuracy and robustness of the proposed models. With high accuracy, this system can play a pivotal role in predicting an upcoming flood, thereby helping to mitigate its risks and safeguard communities.


## Conclusion

In this paper, we present a comprehensive regional study on forecasting water levels in Goslar and Göttingen, Germany, by only using radar-based precipitation data. The study is motivated by the extreme flood events in 2017 in both regions, where water levels rose to 1.59 meters in Goslar and 1.40 meters in Göttingen, causing severe flooding in their respective regions. One of the key contributions of this paper is the innovative approach to addressing the non-linear correlation between precipitation and water levels by predicting the residuals of water levels at sensors.

By incorporating advanced techniques like **transfer learning** and **federated learning**, the model can be extended to various network topologies, accommodating additional atmospheric parameters, such as temperature, humidity, and snowmelt. In conclusion, this study highlights the essential role of integrating precipitation data without the use of upstream data for extreme flood forecasting.

