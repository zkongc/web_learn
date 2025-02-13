import React from 'react';
import VideoItem from './VideoItem';

const VideoList = () => {
  const videos = [
    {
      id: 1,
      title: "视频 1",
      url: "https://example.com/video1",
      duration: 300 // 视频时长（秒）
    },
    {
      id: 2,
      title: "视频 2", 
      url: "https://example.com/video2",
      duration: 400
    }
  ];

  return (
    <div className="video-list">
      <h2>视频列表</h2>
      {videos.map(video => (
        <VideoItem key={video.id} video={video} />
      ))}
    </div>
  );
};

export default VideoList; 