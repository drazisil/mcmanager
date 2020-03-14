const { main } = require('../src')
describe('MCManager', () => {
    it('main() should not throw', () => {
        expect(() => {
            main()
        }).not.toThrow()
    })
})
