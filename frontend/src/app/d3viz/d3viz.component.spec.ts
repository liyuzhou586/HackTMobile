import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { D3vizComponent } from './d3viz.component';

describe('D3vizComponent', () => {
  let component: D3vizComponent;
  let fixture: ComponentFixture<D3vizComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ D3vizComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(D3vizComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
