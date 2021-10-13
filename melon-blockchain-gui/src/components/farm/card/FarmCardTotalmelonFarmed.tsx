import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useSelector } from 'react-redux';
import type { RootState } from '../../../modules/rootReducer';
import FarmCard from './FarmCard';
import { mojo_to_melon } from '../../../util/melon';
import useCurrencyCode from '../../../hooks/useCurrencyCode';
import { FormatLargeNumber } from '@melon/core';

export default function FarmCardTotalmelonFarmed() {
  const currencyCode = useCurrencyCode();

  const loading = useSelector(
    (state: RootState) => !state.wallet_state.farmed_amount,
  );

  const farmedAmount = useSelector(
    (state: RootState) => state.wallet_state.farmed_amount?.farmed_amount,
  );

  const totalmelonFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      const val = BigInt(farmedAmount.toString());
      return mojo_to_melon(val);
    }
  }, [farmedAmount]);

  return (
    <FarmCard
      title={<Trans>{currencyCode} Total mELON Farmed</Trans>}
      value={<FormatLargeNumber value={totalmelonFarmed} />}
      loading={loading}
    />
  );
}
