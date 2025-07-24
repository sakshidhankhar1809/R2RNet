# A Spatiotemporal Radar based Precipitation Model for Water Level Prediction and Flood Forecasting

This repository contains the code for the paper "A Spatiotemporal Radar-Based Precipitation Model for Water Level Prediction and Flood Forecasting".


## Introduction

This paper introduces the Spatial-Temporal Radar-based Precipitation Model (STRPM), a novel approach designed to integrate radar-derived precipitation data with river water levels measured in Goslar. By capturing the dynamic nature of precipitation events, STRPM aims to improve the lead time and reliability of flood forecasts. This model addresses the limitations of limited upstream data by incorporating high-frequency radar observations, which offer detailed insights into the spatial distribution and intensity of rainfall. The primary objectives of this research are to develop and validate the STRPM, assess its performance in various scenarios, and demonstrate its potential for operational flood forecasting. The model's performance is systematically evaluated using the original Goslar Benchmark: https://www.scitepress.org/Link.aspx?doi=10.5220/0012081700003546 together with additional experiments to assess its accuracy. To validate the model's robustness, additional testing was conducted on data from Göttingen. This validation demonstrated the model's flexibility, indicating its potential for future implementation in regions with varying topologies through the application of transfer-learning techniques.


## Abstract

***Study Region:*** Goslar and Göttingen, Lower Saxony, Germany.

***Study Focus:*** In July 2017, the cities of Goslar and Göttingen experienced severe flood events characterized by short warning time of only 20 minutes, resulting in extensive regional flooding and significant damage. This highlights the critical need for a more reliable and timely flood forecasting system. This paper presents a comprehensive study on the impact of radar-based precipitation data on forecasting river water levels in Goslar. Additionally, the study examines how precipitation influences water level forecasts in Göttingen. The analysis integrates radar-derived spatiotemporal precipitation patterns with hydrological sensor data obtained from ground stations to evaluate the effectiveness of this approach in improving flood prediction capabilities. 

***New Hydrological Insights for the Region:*** A key innovation in this paper is the use of residual-based modeling to address the non-linearity between precipitation images and water levels, leading to a Spatiotemporal Radar-based Precipitation Model with residuals (STRPMr). Unlike traditional hydrological models, our approach does not rely on upstream data, making it independent of additional hydrological inputs. This independence enhances its adaptability and allows for broader applicability in other regions with RADOLAN precipitation. The deep learning architecture integrates (2+1)D convolutional neural networks for spatial and temporal feature extraction with LSTM for timeseries forecasting. The results demonstrate the potential of the STRPMr for capturing extreme events and more accurate flood forecasting.


## Data

This paper utilizes three datasets, one of which is the publicly available ground-based RADAR precipitation dataset from the DWD: https://opendata.dwd.de/climate_environment/CDC/grids_germany/5_minutes/radolan/reproc/2017_002/asc/, the national meteorological service of Germany. The dataset consists of Radar Online Calibration (RADOLAN) precipitation images, which are provided at a temporal resolution of 5-minute intervals and a spatial resolution of 1 km x 1 km. The selected time period for analysis spans from November 1, 2003, to June 30, 2018, covering approximately 15 years of continuous precipitation data. 

The second dataset comprises water level measurements for Goslar recorded at Sennhuette hydrological sensor station provided by Harzwasserwerke GmbH, corresponding to the same time interval. These water level measurements are captured at a temporal resolution of 15-minute intervals and serve as the target variable in our experiments for Goslar. 

The third dataset comprises water level measurements for Göttingen provided by Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz (NLWKN), corresponding to the same time interval with 15-minutes resolution. This dataset is used for validation purposes in this paper.


## Performance evaluation

The performance of this model can be evaluated using various overall metrics such as *Nash Sucliffe efficiency(NSE)*, *Index of agreement (IoA)*, *Mean squared error(MSE)* and *Bravais-Pearson (BP)*, to assess the accuracy and robustness of the proposed models. With high accuracy, this system can play a pivotal role in predicting an upcoming flood, thereby helping to mitigate its risks and safeguard communities.


## Conclusion

In this paper, we present a comprehensive regional study on forecasting water levels in Goslar and Göttingen, Germany, by only using radar-based precipitation data. The study is motivated by the extreme flood events in 2017 in both regions, where water levels rose to 1.59 meters in Goslar and 1.40 meters in Göttingen, causing severe flooding in their respective regions. One of the key contributions of this paper is the innovative approach to addressing the non-linear correlation between precipitation and water levels by predicting the residuals of water levels at sensors.

By incorporating advanced techniques like **transfer learning** and **federated learning**, the model can be extended to various network topologies, accommodating additional atmospheric parameters, such as temperature, humidity, and snowmelt. In conclusion, this study highlights the essential role of integrating precipitation data without the use of upstream data for extreme flood forecasting.