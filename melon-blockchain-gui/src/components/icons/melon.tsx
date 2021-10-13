import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as melonIcon } from './images/melon.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={melonIcon} viewBox="0 0 82 100" {...props} />;
}
