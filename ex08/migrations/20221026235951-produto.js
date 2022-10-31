'use strict';

module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.createTable('produtos', {
      registro: { 
          allowNull: false,
          autoIncrement: true,
          primaryKey: true,
          type: Sequelize.DataTypes.INTEGER
      },

      autor: {
        allowNull: false,
        type: Sequelize.DataTypes.STRING
      },
      titulo: {
        allowNull: false,
        type: Sequelize.DataTypes.STRING
      },
      editora: {
        allowNull: false,
        type: Sequelize.DataTypes.STRING
      },
      ano: {
        allowNull: false,
        type: Sequelize.DataTypes.INTEGER
      },

      quantidade: {
        allowNull: false,
        type: Sequelize.DataTypes.INTEGER
      },

      valor: {
        allowNull: false,
        type: Sequelize.DataTypes.INTEGER
      }
    })
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.dropTable('produtos')
  }
};
