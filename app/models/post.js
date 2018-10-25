import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr('string'),
    auther: DS.attr('string'),
    slug: DS.attr('string'),
    description: DS.attr('string'),
    tags: DS.attr('string'),
});
