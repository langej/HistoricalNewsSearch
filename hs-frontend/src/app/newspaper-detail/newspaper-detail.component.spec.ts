import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewspaperDetailComponent } from './newspaper-detail.component';

describe('NewspaperDetailComponent', () => {
  let component: NewspaperDetailComponent;
  let fixture: ComponentFixture<NewspaperDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewspaperDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewspaperDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
