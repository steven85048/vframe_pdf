import React from 'react';

import VideoPlayer from './VideoPlayer';

export default function VideoEditor() {
  const handleVideoProgressChange = (progress) => {
    console.log(progress);
  }

  return (
    <div>
        <VideoPlayer 
            youtubeUrl="https://www.youtube.com/watch?v=DNMO-MdmO6g&ab_channel=HiroshiNakamura"
            onVideoProgress={handleVideoProgressChange}/>
    </div>
  );
}
