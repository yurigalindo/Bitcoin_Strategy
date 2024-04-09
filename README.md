# Bitcoin Buying and Selling Strategies

This is a toy project that aims to build and compare trading models for buying and selling bitcoin.
My goal is to practice software architecture and design, and OOP in python. Possibly improve my skill in time-series forecasting along the way.

Disclaimer: this is not an endorsement of cryptocurrency or any trading strategy, just programming practice. Following any of these strategies may result in financial loss.

## Roadmap
~~Implement 2 traditional trading strategies~~
~~Compare using various parameters~~

    3. Implement 3 machine learning models
    4. Compare using various parameters
    5. Make real-time decisions by making API calls 

## Software Architecture and Design

I have identified a problem in the BuySellModel class: if the trade_signal method changes state used by the trade_order method or vice-versa, this adds complexity and potentially unwanted behavior. So I want to delegate these two methods to different classes, and orchestrate the two objects using BuySellModel

### Diagrams

To-Do:

    1. Class Diagram
    2. Sequence Diagram
    3. Use-case Diagram
