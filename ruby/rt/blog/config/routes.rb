Rails.application.routes.draw do
  resources :articles
  root 'welcome#index'
  get 'welcome/index'
end
