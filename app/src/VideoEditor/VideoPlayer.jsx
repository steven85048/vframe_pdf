import React from 'react';
import PropTypes from 'prop-types';

import ReactPlayer from 'react-player';

export default function VideoPlayer({youtubeUrl, handleVideoProgressChange}) {
  const handleProgressChange = (progress) => {
    handleVideoProgressChange(progress);
  };

  return (
    <div>
      <ReactPlayer 
        progressInterval = {500}
        onProgressChange = {handleProgressChange} 
        url={youtubeUrl} />
    </div>
  );
}

VideoPlayer.propTypes = {
    youtubeUrl: PropTypes.string.isRequired,
    handleVideoProgressChange: PropTypes.func.isRequired
};
