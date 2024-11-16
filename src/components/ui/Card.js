// src/components/ui/Card.js
import React from 'react';

export const Card = ({ children, className }) => {
  return (
    <div className={`border rounded-lg shadow-md p-4 ${className}`}>
      {children}
    </div>
  );
};

export const CardHeader = ({ children }) => {
  return (
    <div className="border-b pb-2 mb-2">
      {children}
    </div>
  );
};

export const CardContent = ({ children, className }) => {
  return (
    <div className={`content ${className}`}>
      {children}
    </div>
  );
};