// src/AgePredictionDemo.js
import React, { useState } from 'react';
import { Card, CardHeader, CardContent } from './components/ui/Card'; // Adjust path if necessary
import { Brain, Upload, Gauge, Users } from 'lucide-react';

const AgePredictionDemo = () => {
  const [activeTab, setActiveTab] = useState('overview');

  const stats = [
    {
      icon: <Brain className="w-6 h-6 text-purple-500" />,
      label: "CNN Architecture",
      value: "Advanced Deep Learning"
    },
    {
      icon: <Upload className="w-6 h-6 text-blue-500" />,
      label: "Training Dataset",
      value: "20,000+ Images"
    },
    {
      icon: <Gauge className="w-6 h-6 text-green-500" />,
      label: "Real-time Processing",
      value: "< 2s Response"
    },
    {
      icon: <Users className="w-6 h-6 text-orange-500" />,
      label: "Active Users",
      value: "1,000+"
    }
  ];

  return (
    <div className="w-full max-w-4xl p-4 space-y-6">
      {/* Project Header */}
      <div className="space-y-2">
        <h1 className="text-3xl font-bold text-gray-900">Age Prediction AI</h1>
        <p className="text-gray-600">Instantly predict age from photos using advanced AI</p>
      </div>

      {/* Tech Stack Tags */}
      <div className="flex flex-wrap gap-2">
        {['Python', 'TensorFlow', 'Streamlit', 'OpenCV', 'Keras'].map((tech) => (
          <span key={tech} className="px-3 py-1 text-sm font-medium text-purple-600 bg-purple-50 rounded-full">
            {tech}
          </span>
        ))}
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, index) => (
          <Card key={index} className="hover:shadow-lg transition-shadow">
            <CardContent className="p-4">
              <div className="flex flex-col items-center space-y-2">
                <div className="p-2 bg-gray-50 rounded-full">
                  {stat.icon}
                </div>
                <p className="text-lg font-semibold">{stat.value}</p>
                <p className="text-sm text-gray-600">{stat.label}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Project Features */}
      <Card className="mt-6">
        <CardHeader>
          <h2 className="text-xl font-semibold">Key Features</h2>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="flex items-start space-x-3">
              <div className="p-2 bg-green-50 rounded-lg">
                <Upload className="w-5 h-5 text-green-600" />
              </div>
              <div>
                <h3 className="font-medium">Easy Upload</h3>
                <p className="text-sm text-gray-600">Drag and drop images or click to upload.</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="p-2 bg-blue-50 rounded-lg">
                <Gauge className="w-5 h-5 text-blue-600" />
              </div>
              <div>
                <h3 className="font-medium">Fast Predictions</h3>
                <p className="text-sm text-gray-600">Get results in under 2 seconds.</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="p-2 bg-yellow-50 rounded-lg">
                <Users className="w-5 h-5 text-yellow-600" />
              </div>
              <div>
                <h3 className="font-medium">User -Friendly Interface</h3>
                <p className="text-sm text-gray-600">Intuitive design for all users.</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="p-2 bg-red-50 rounded-lg">
                <Brain className="w-5 h-5 text-red-600" />
              </div>
              <div>
                <h3 className="font-medium">AI-Powered</h3>
                <p className="text-sm text-gray-600">Utilizes state-of-the-art AI technology.</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AgePredictionDemo;