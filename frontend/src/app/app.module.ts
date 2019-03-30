import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PhoneComponent } from './phone/phone.component';
import { BackendService } from './services/backend.service';
import { D3vizComponent } from './d3viz/d3viz.component';

@NgModule({
  declarations: [
    AppComponent,
    PhoneComponent,
    D3vizComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [BackendService],
  bootstrap: [AppComponent]
})
export class AppModule { }
