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

Initially, I had one class containing methods for deciding when to buy, and another method deciding how much to buy. However, I realized that when both of these metehods change atributes of the class, this can add a bunch of complexity and unwanted behavior. So I refactored to delegate this to two objects: a signal modeling object, and an allocation object. This also opened up an easy way to re-use allocation strategies, specially when using Machine Learning models, since this decision doesn't depend on the type of model being used.

### Diagrams

To-Do:

    1. Class Diagram
    2. Sequence Diagram
    3. Use-case Diagram
