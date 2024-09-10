require 'sinatra'
require 'mongoid'


Mongoid.load!(File.join(File.dirname(__FILE__), 'config', 'mongoid.yml'))

get '/samples' do

    { "answer" => "Hi!"}.to_json

end

get '/samples/:sample_id' do |sample_id|
    sample = Sample.find(sample_id)
    
    sample.to_json

end

post '/samples' do

    sample = Sample.create!(params[:sample])
    sample.to_json

end

class Sample

    include Mongoid::Document

    field :id, type: String
    field :taxon, type: String

end
