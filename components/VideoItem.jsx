import React, { useEffect, useState } from 'react';

const VideoItem = ({ video }) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // 从 localStorage 获取观看进度
    const savedProgress = localStorage.getItem(`video-${video.id}-progress`);
    if (savedProgress) {
      setProgress(parseInt(savedProgress));
    }
  }, [video.id]);

  const handleVideoClick = () => {
    // 在新窗口打开视频
    window.open(video.url, '_blank');
    
    // 更新观看进度（这里简单模拟，实际应该根据真实观看时间更新）
    const newProgress = Math.min(progress + 10, 100);
    setProgress(newProgress);
    localStorage.setItem(`video-${video.id}-progress`, newProgress.toString());
  };

  return (
    <div className="video-item">
      <h3>{video.title}</h3>
      <div className="progress-bar">
        <div 
          className="progress" 
          style={{ width: `${progress}%` }}
        ></div>
      </div>
      <button onClick={handleVideoClick}>观看视频</button>
      <span>观看进度: {progress}%</span>
    </div>
  );
};

export default VideoItem; 