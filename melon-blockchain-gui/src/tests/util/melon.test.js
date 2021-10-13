const melon = require('../../util/melon');

describe('melon', () => {
  it('converts number mojo to melon', () => {
    const result = melon.mojo_to_melon(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to melon', () => {
    const result = melon.mojo_to_melon('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to melon string', () => {
    const result = melon.mojo_to_melon_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to melon string', () => {
    const result = melon.mojo_to_melon_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number melon to mojo', () => {
    const result = melon.melon_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string melon to mojo', () => {
    const result = melon.melon_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = melon.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = melon.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = melon.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = melon.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = melon.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = melon.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
