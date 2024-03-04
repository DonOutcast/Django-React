import React, {useState} from 'react';
import './App.css';
import DistributionStatistics from "./components/DistrubutionStatistic";
import DistributionList from "./components/Distribution";

function App() {
  const [selectedDistributionId, setSelectedDistributionId] = useState<number | null>(null);

  const handleSelectDistribution = (id: number) => {
    setSelectedDistributionId(id);
  };

  return (
    <div className="app-container">
      <DistributionList />
    </div>
  );
}

export default App;