import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SearchbarComponent} from "./searchbar/searchbar.component";

const routes: Routes = [
  {
    path: '',
    redirectTo: 'search',
    pathMatch: 'full'
  },
  {
    path: 'search',
    component: SearchbarComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule { }
