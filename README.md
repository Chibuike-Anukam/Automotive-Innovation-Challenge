# Real-Time Parking Spot Finder

An AI-powered computer vision system that analyzes infrastructure camera feeds to identify available parking spots in real-time.

## Overview
This project was developed as part of the Automotive Innovation Challenge hosted by Western Engineering in partnership with General Motors. The challenge focused on creating innovative solutions for urban mobility problems using cutting-edge technology.
The system addresses the common urban problem of finding available parking by leveraging existing infrastructure cameras and AI-powered computer vision to provide real-time parking availability information to users.

### Key Features:
- Real-time parking spot detection using computer vision
- AI model trained on large dataset for accurate identification
- Web-based user interface for easy access to parking information (named 'Smart Park' by team)
- Integration with existing infrastructure cameras
- Scalable system design for multiple parking locations

## Challenge Specifications
- Event: Automotive Innovation Challenge
- Organizer: Western Engineering & General Motors
- Duration: 3-day intensive build timeline
- Team Size: 4-person collaborative team
- Evaluation: Comprehensive criteria including technical implementation, user experience, and innovation
- Timeline: March 2025

## System Architecture
### Computer Vision Pipeline:
- Infrastructure camera feed input
- YOLO AI model for object detection and classification
- Real-time image processing for parking spot analysis
- Status determination (occupied/vacant) for each parking space
### Data Processing:
- Large-scale dataset training (6,800 images)
- Model retraining for parking-specific optimization
- Real-time inference on camera feeds
- Aggregation of parking availability data
### User Interface:
- Web-based application for user accessibility
- Real-time parking availability display

## Technical Implementation
### AI/Machine Learning:
- Model: YOLO (You Only Look Once) for real-time object detection
- Framework: Python-based implementation
- Training Data: 6,800 labeled parking spot images
- Optimization: Model retraining for parking-specific detection accuracy
- Performance: Real-time processing capability
### Computer Vision:
- Infrastructure camera integration
- Parking spot boundary detection
- Occupancy status classification
### Web Application:
- Frontend user interface development
- Real-time data visualization
- Responsive design for multiple devices

## Development Process
### Day 1: Planning & Setup
- Problem analysis and solution design
- Team role assignment and project planning
### Day 2: Core Development
- Architecture design and technology selection
- AI model setup and training
- Computer vision pipeline implementation
- Web interface development
- Integration testing and debugging
### Day 3: Integration & Presentation
- System integration and final testing
- User interface refinement
- Presentation preparation and practice
- Final evaluation and demonstration

## Results & Achievements
### Technical Outcomes:
- Unsuccessfully retrained YOLO model for parking spot detection (failed after 3/100 epochs)
- Implemented web-based user interface, but could not connect model as an API in backend
### Learning Outcomes:
- Project Management: Intensive 3-day project timeline management
- AI/ML Development: Hands-on experience with YOLO model training and optimization
- Computer Vision: Practical application of image processing techniques
- Web Development: Full-stack development for real-time data visualization
- Team Collaboration: Effective 4-person team coordination under time pressure

### Innovation Impact:
- Addresses real urban mobility challenges
- Leverages existing infrastructure efficiently
- Scalable solution for smart city applications
- Practical implementation of AI in automotive industry

## Project Team & Collaboration
### Team Structure:
- 4-person multidisciplinary team
- Roles: AI/ML development, computer vision, web development, project coordination
- Collaborative development using modern software practices

## Event Information
### Challenge Details:
- Host: Western Engineering, University of Western Ontario
- Industry Partner: General Motors
- Focus: Automotive innovation and smart mobility solutions
- Format: Intensive 3-day hackathon-style competition
- Evaluation: Technical implementation, innovation, presentation, and real-world applicability

## Documentation & Resources
### Development Artifacts:
- Trained YOLO model weights and configuration
- Training and validation images and labels from dataset
- Web application source code


This project demonstrates the practical application of AI and computer vision technologies to solve real-world urban mobility challenges. Developed under intensive timeline constraints, it showcases rapid prototyping, team collaboration, and innovative problem-solving skills.

Team Achievement: Successful completion of Automotive Innovation Challenge
Institution: University of Western Ontario, Western Engineering
Industry Partner: General Motors
Date: March 2025
