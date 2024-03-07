describe('Test ID Page', () => {
    it('passes', () => {
        cy.visit(Cypress.env('url') + '/page/1') // Replace '/id-page' with the actual URL of your ID page
        cy.get('body').should('contain', 'Page 1')
    })
})
