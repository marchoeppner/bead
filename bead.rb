require 'sinatra'
require 'mongoid'


Mongoid.load!(File.join(File.dirname(__FILE__), 'config', 'mongoid.yml'))

get '/samples' do

    Sample.all.to_json

end

get '/samples/:sample_id' do |sample_id|

    sample = Sample.find(sample_id)
    sample.attributes.merge(
        alleles: sample.alleles,
    ).to_json

end

post '/samples' do

    json = JSON.parse(request.body.read)
    json["created_at"] = Time.now
    sample = Sample.create!(json)
    sample.to_json
    
end

post '/samples/:sample_id/alleles' do |sample_id|
    json = JSON.parse(request.body.read)
    json["created_at"] = Time.now
    sample = Sample.find(sample_id)
    alleles = sample.alleles.create!(json)
    alleles.to_json
end

get '/samples/delete/:sample_id' do |sample_id|
    sample = Sample.find(sample_id)
    sample.delete
    sample.to_json
end


class Sample

    include Mongoid::Document
    include Mongoid::Timestamps
    include Mongoid::Attributes::Dynamic

    has_many :alleles

    field :id, type: String
    field :amrfinder, type: String
    field :sample, type: String
    field :created_at, type: DateTime

    validates_presence_of :sample
end

class Allele

    include Mongoid::Document
    include Mongoid::Timestamps

    belongs_to :sample

    field :id, type: String
    #field :sample_id, type: String
    field :profile, type: String
    field :cgmlst_scheme, type: String
    field :cgmlst_scheme_version, type: String
    field :created_at, type: DateTime

    validates_presence_of :profile, :cgmlst_scheme, :cgmlst_scheme_version

end
