describe('Frank Page exists with correct text', () => {
    it('passes', () => {
      cy.visit(Cypress.env('url'))+'/frank'
      cy.get('body').should('contain', 'frank Page at')
    })
  })