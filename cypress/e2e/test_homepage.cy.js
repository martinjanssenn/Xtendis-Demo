describe('Home Page exists with correct text', () => {
  it('passes', () => {
    cy.visit(Cypress.env('url'))
    cy.get('body').should('contain', 'Home Page')
  })
})